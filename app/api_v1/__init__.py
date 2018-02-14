#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29 14:24
# @Author  : Vniex
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm
from flask import Blueprint
from flask_restful import Api, fields
from flask_restful_extend import support_jsonp

api_blueprint = Blueprint("api", __name__, url_prefix='/api')
api = Api(api_blueprint)

support_jsonp(api)
from . import blocks