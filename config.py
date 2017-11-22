#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/28 21:09
# @Author  : Vniex
# @Site    :
# @File    : models.py
# @Software: PyCharm
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              # 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    MYSQL_IP='localhost'
    MYSQL_PORT = '3306'
    MYSQL_USERNAME='root'
    MYSQL_PASSWORD='zb555920'
    MYSQL_DB='openblocks'
    MYSQL_CHARSET='charset=utf8'
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://" +MYSQL_USERNAME+":"+MYSQL_PASSWORD+"@"+MYSQL_IP+":"+MYSQL_PORT+"/"+MYSQL_DB+'?'+MYSQL_CHARSET
