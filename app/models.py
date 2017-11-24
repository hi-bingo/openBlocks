#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/28 21:09
# @Author  : Vniex
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from sqlalchemy import Column, Integer, String,Text,DateTime,DECIMAL,BigInteger
from app import db


class BlockProjectBase(db.Model):
    __tablename__ = 'projectBase'
    id = Column(Integer, primary_key=True,)
    name = Column(String(255), unique=True)
    fullName = Column(String(255))
    website = Column(String(255))
    whitepaper = Column(String(255))
    desp = Column(Text)


class BlockProjectGit(db.Model):
    __tablename__ = 'projectGit'
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(255),unique=True)
    gitAddress = Column(String(255))
    star=Column(Integer)
    forks=Column(Integer)
    openIssue=Column(Integer)
    releases = Column(Integer)
    contributors = Column(Integer)
    lastCommit=Column(DateTime)
    weekCommit=Column(Integer)
    monthCommit = Column(Integer)
    seasonCommit = Column(Integer)


class BlockProjectPrice(db.Model):
    __tablename__ = 'projectPrice'
    id = Column(Integer,autoincrement=True, primary_key=True)
    name = Column(String(255),unique=True)
    supply=Column(BigInteger)
    amount = Column(String(255))
    currentPriceCNY=Column(DECIMAL(30,4))
    marketPriceCNY=Column(DECIMAL(30,4))
    currentPriceUSD = Column(DECIMAL(30,4))
    marketPriceUSD = Column(DECIMAL(30,4))