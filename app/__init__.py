#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/28 21:09
# @Author  : Vniex
# @Site    :
# @File    : models.py
# @Software: PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

# from app.api_v1.api import api

db = SQLAlchemy()
api = Api()


from app.api_v1 import api_blueprint

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    # config[config_name].init_app(app)

    db.init_app(app)
    # api.init_app(app)
    app.register_blueprint(api_blueprint)
    # attach routes and custom error pages here
    cors = CORS(app, resources={"/api/*": {"origins": "*"}})
    return app
