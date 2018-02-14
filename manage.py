#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/28 21:09
# @Author  : Vniex
# @Site    :
# @File    : models.py
# @Software: PyCharm
from app import create_app, db
from app.models import BlockProjectBase, BlockProjectGit,BlockProjectPrice  # 注册数据库模型
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand  # 载入migrate扩展
import config

app=create_app(config.Config)
manager = Manager(app)
migrate = Migrate(app, db)  # 注册migrate到flask

manager.add_command('db', MigrateCommand)  # 在终端环境下添加一个db命令

if __name__ == '__main__':
    manager.run()