#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 22:04
# @Author  : Vniex
# @Site    : 
# @File    : githubSpider.py
# @Software: PyCharm
import sys

sys.path.append("..")
from gevent import monkey;

monkey.patch_all()
import time, threading
import requests, gevent
import dateutil.parser
import logging, json, datetime
from dateutil import tz

from sqlalchemy import Column, String, Integer, DateTime, Text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
from app.models import BlockProjectGit, BlockProjectPrice

Base = declarative_base()

engine = create_engine(config.DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
DBSession = sessionmaker(bind=engine)

FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=FORMAT, filename='spider.log', level=logging.INFO)




def ts2date(ts):
    return datetime.datetime.fromtimestamp(
        int(ts)
    ).strftime('%m/%d')


def parseBaseUrl(baseUrl, headers):
    res = requests.get(baseUrl, headers=headers).json()
    return res['stargazers_count'], res['forks_count'], res['open_issues_count'], res['subscribers_count']


def parsecontributorsUrl(contributorsUrl, headers):
    res = requests.get(contributorsUrl, headers=headers).json()
    return len(res)


def parsecommitUrl(commitUrl, headers):
    res = requests.get(commitUrl, headers=headers).json()
    commitStats = []
    for week in res:
        commitStats.append((ts2date(week['week']), week['total']))

    return res[-1]['total'], sum(x['total'] for x in res[-4:]), sum(x['total'] for x in res[-12:]), json.dumps(
        commitStats)


def parsereleaseUrl(releaseUrl, headers):
    res = requests.get(releaseUrl, headers=headers).json()
    return len(res)


def parselastCommitUrl(lastCommitUrl, headers):
    res = requests.get(lastCommitUrl, headers=headers).json()
    return dateutil.parser.parse(res[0]['commit']['committer']['date']).astimezone(tz.tzlocal())


def scrapyProjectGit(projectGit):
    headers = {'authorization': config.Config.GITHUB_AUTH}
    URL_PRE = 'https://api.github.com/repos/'
    repo = projectGit.gitAddress.split('https://github.com/')[1]
    baseUrl = URL_PRE + repo
    contributorsUrl = URL_PRE + repo + '/stats/contributors'
    commitUrl = URL_PRE + repo + '/stats/commit_activity'
    releaseUrl = URL_PRE + repo + '/releases'
    lastCommitUrl = URL_PRE + repo + '/commits'
    try:
        taskList = [gevent.spawn(parseBaseUrl, baseUrl, headers),
                    gevent.spawn(parsecontributorsUrl, contributorsUrl, headers),
                    gevent.spawn(parsecommitUrl, commitUrl, headers),
                    gevent.spawn(parsereleaseUrl, releaseUrl, headers),
                    gevent.spawn(parselastCommitUrl, lastCommitUrl, headers),
                    ]
        gevent.joinall(taskList)
        projectGit.star, projectGit.forks, projectGit.openIssue, projectGit.watch = taskList[0].value
        print(taskList[0].value)
        projectGit.contributors = taskList[1].value
        projectGit.weekCommit, projectGit.monthCommit, projectGit.seasonCommit, projectGit.commitStats = taskList[
            2].value
        projectGit.releases = taskList[3].value
        projectGit.lastCommit = taskList[4].value
    except Exception as e:
        logging.error(e)

    return projectGit


def scrapyGithub():
    logging.info('scrapy github....')
    try:
        session = DBSession()
        projectGits = session.query(BlockProjectGit).all()
        taskList = []
        for projectGit in projectGits:
            taskList.append(gevent.spawn(scrapyProjectGit, projectGit))
        gevent.joinall(taskList)
        session.commit()
        session.close()
    except Exception as e:
        print('github:')
        print(e)
        logging.error(e)


def scrapyAicoin():
    logging.info('scrapy aicoin....')
    usd2cny = 6.6
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }
    try:
        session = DBSession()
        projectPrices = session.query(BlockProjectPrice).all()
        try:
            rate = requests.get('https://www.okex.com/api/v1/exchange_rate.do', headers=headers).json()
            usd2cny = float(rate['rate'])
        except:
            logging.error('okex api error')
        aiCoinUrl = 'https://aicoin.com/api/data/getMc?type=all'
        result = requests.get(aiCoinUrl).json()
        coinDict = {}
        for coin in result:
            coinDict[coin['lowerName']] = coin
        for projectPrice in projectPrices:
            if projectPrice.name in coinDict:
                projectPrice.amount = coinDict[projectPrice.name]['amount']
                projectPrice.supply = coinDict[projectPrice.name]['supply']
                projectPrice.currentPriceCNY = float(coinDict[projectPrice.name]['price'])
                projectPrice.marketPriceCNY = float(coinDict[projectPrice.name]['mc'])
                projectPrice.currentPriceUSD = projectPrice.currentPriceCNY / usd2cny
                projectPrice.marketPriceUSD = projectPrice.marketPriceCNY / usd2cny
        session.commit()
    except Exception as e:
        print('aicoin:')
        print(e)
        logging.error(e)


if __name__ == '__main__':
    # print(config.DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
    # session = DBSession()
    # projectGits = session.query(BlockProjectGit).all()
    # for projectGit in projectGits:
    #     print(projectGit.name)
    #     print(projectGit.gitAddress)
    gitFlag = True
    gitCount=0
    while True:
        aicoinSpider = threading.Thread(target=scrapyAicoin, name='scrapyAicoin')
        aicoinSpider.start()

        if gitFlag:
            gitFlag = False
            githubSpider = threading.Thread(target=scrapyGithub, name='scrapyGithub')
            githubSpider.start()

        time.sleep(config.Config.AICOIN_INTERVAL)
        gitCount += 1
        if (gitCount >= config.Config.GITHUB_INTERVAL/config.Config.AICOIN_INTERVAL):
            gitCount = 0
            gitFlag = True
