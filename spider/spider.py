#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 22:04
# @Author  : Vniex
# @Site    : 
# @File    : githubSpider.py
# @Software: PyCharm
import sys
sys.path.append("..")
import requests
import dateutil.parser
from dateutil import tz
import time,threading
from sqlalchemy import Column, String, Integer,DateTime,Text,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
from app.models import BlockProjectGit


Base = declarative_base()

engine = create_engine(config.DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
DBSession = sessionmaker(bind=engine)


# def scrapy(project):
#     response = requests.get(project.gitAddress)
#     selector = html.fromstring(response.text)
#     project.star = int(
#         selector.xpath('//*[@id="js-repo-pjax-container"]/div[1]/div/ul/li[2]/a[2]/text()')[0].strip().replace(',', ''))
#     status = selector.xpath('//*[@class="stats-switcher-viewport js-stats-switcher-viewport"]/div/ul/li')
#     project.commit = int(status[0].xpath('a/span/text()')[0].strip().replace(',', ''))
#     project.branches = int(status[1].xpath('a/span/text()')[0].strip().replace(',', ''))
#     project.releases = int(status[2].xpath('a/span/text()')[0].strip().replace(',', ''))
#     project.contributors = int(status[3].xpath('a/span/text()')[0].strip().replace(',', ''))
#     lastMod= \
#     dateutil.parser.parse(selector.xpath('//*[@class="commit-tease js-details-container Details"]/span[1]/span/relative-time/@datetime')[0])
#
#
#     project.lastCommit=lastMod.astimezone(tz.tzlocal())
#     print(project.lastCommit)

def scrapyGithub():
    while True:
        print('scrapy github....')
        time.sleep(5)


def scrapyAicoin():
    while True:
        print('scrapy aicoin....')
        time.sleep(3)




if __name__ == '__main__':
    # print(config.DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
    # session = DBSession()
    # projectGits = session.query(BlockProjectGit).all()
    # for projectGit in projectGits:
    #     print(projectGit.name)
    #     print(projectGit.gitAddress)
    githubSpider = threading.Thread(target=scrapyGithub, name='scrapyGithub')
    aicoinSpider = threading.Thread(target=scrapyAicoin, name='scrapyAicoin')
    githubSpider.start()
    aicoinSpider.start()
