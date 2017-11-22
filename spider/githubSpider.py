#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 22:04
# @Author  : Vniex
# @Site    : 
# @File    : githubSpider.py
# @Software: PyCharm
import requests
import dateutil.parser
from dateutil import tz
from lxml import html
from sqlalchemy import Column, String, Integer,DateTime,Text,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("mysql+pymysql://root:zb555920@127.0.0.1:3306/openblocks")
DBSession = sessionmaker(bind=engine)

class BlockProject(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name=Column(String(255), unique=True)
    fullName=Column(String(255))

    star=Column(Integer)
    branches=Column(Integer)
    releases = Column(Integer)
    contributors = Column(Integer)
    lastCommit=Column(DateTime)

    gitAddress=Column(String(255))
    website = Column(String(255))
    whitepaper=Column(String(255))
    desp=Column(Text)




def scrapy(project):
    response = requests.get(project.gitAddress)
    selector = html.fromstring(response.text)
    project.star = int(
        selector.xpath('//*[@id="js-repo-pjax-container"]/div[1]/div/ul/li[2]/a[2]/text()')[0].strip().replace(',', ''))
    status = selector.xpath('//*[@class="stats-switcher-viewport js-stats-switcher-viewport"]/div/ul/li')
    project.commit = int(status[0].xpath('a/span/text()')[0].strip().replace(',', ''))
    project.branches = int(status[1].xpath('a/span/text()')[0].strip().replace(',', ''))
    project.releases = int(status[2].xpath('a/span/text()')[0].strip().replace(',', ''))
    project.contributors = int(status[3].xpath('a/span/text()')[0].strip().replace(',', ''))
    lastMod= \
    dateutil.parser.parse(selector.xpath('//*[@class="commit-tease js-details-container Details"]/span[1]/span/relative-time/@datetime')[0])


    project.lastCommit=lastMod.astimezone(tz.tzlocal())
    print(project.lastCommit)






if __name__ == '__main__':
    session = DBSession()
    projects = session.query(BlockProject).all()
    for project in projects:
        scrapy(project)
    session.commit()