#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/24 16:14
# @Author  : Vniex
# @Site    :
# @File    : Utils.py
# @Software: PyCharm
import requests
import os

staticDir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def parseIcon(iconUrl,saveName):
    ir = requests.get(iconUrl)
    print(staticDir)
    sz = open(staticDir+'/static/'+saveName+'.png', 'wb').write(ir.content)
    print('logo.jpg', sz, 'bytes')
    return saveName+'.png'

def price2float(price):
    if price is None:
        return '/'
    else:
        return float(price)
