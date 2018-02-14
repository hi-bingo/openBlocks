#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/28 21:09
# @Author  : Vniex
# @Site    :
# @File    : models.py
# @Software: PyCharm
import os


class Config:
    DEBUG = True

    MYSQL_IP='localhost'
    MYSQL_PORT = '3306'
    MYSQL_USERNAME='root'
    MYSQL_PASSWORD='zb555920'
    MYSQL_DB='openblocks'
    MYSQL_CHARSET='charset=utf8'
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://" +MYSQL_USERNAME+":"+MYSQL_PASSWORD+"@"+MYSQL_IP+":"+MYSQL_PORT+"/"+MYSQL_DB+'?'+MYSQL_CHARSET

    ##GitHub 账户auth token    "https://developer.github.com/v3/#oauth2-token-sent-in-a-header"
    GITHUB_AUTH="token 894d1d909764c3e6aa1be6952e3668d17484a8d2"

    ##爬取间隔
    GITHUB_INTERVAL = 30 * 60
    AICOIN_INTERVAL = 30