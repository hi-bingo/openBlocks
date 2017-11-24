#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29 0:02
# @Author  : Vniex
# @Site    : 
# @File    : news.py
# @Software: PyCharm
import codecs
import simplejson as json
from flask_restful import Resource,reqparse
from app.models import BlockProjectBase,BlockProjectGit,BlockProjectPrice
from app.api_v1 import api
from app import db

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('fullname', type=str)
parser.add_argument('gitAddress', type=str)
parser.add_argument('website', type=str)
parser.add_argument('whitepaper', type=str)
parser.add_argument('desp', type=str)




class ProjectList(Resource):
    def get(self):
        res=[]
        for base,git,price in db.session.query(BlockProjectBase, BlockProjectGit,BlockProjectPrice).\
                                                filter(BlockProjectBase.name == BlockProjectGit.name).\
                                                filter(BlockProjectBase.name== BlockProjectPrice.name).\
                                                order_by(db.desc(BlockProjectGit.star)).all():
            res.append({'name':base.name,'gitAddress':git.gitAddress,'star':git.star,'forks':git.forks,'contributors':git.contributors,
                 'lastCommit':str(git.lastCommit),'weekCommit':git.weekCommit,'monthCommit':git.monthCommit,'seasonCommit':git.seasonCommit,
                 'releases':git.releases,'marketPriceCNY':float(price.marketPriceCNY)})
        return res

class ProjectDetail(Resource):
    def get(self,coinname):
        base=db.session.query(BlockProjectBase).filter(BlockProjectBase.name == coinname).first()
        git = db.session.query(BlockProjectGit).filter(BlockProjectGit.name == coinname).first()
        price=db.session.query(BlockProjectPrice).filter(BlockProjectPrice.name == coinname).first()
        res={'name': base.name, 'fullName':base.fullName,'website':base.website,'whitepaper':base.whitepaper,
             'desp':base.desp,
             'gitAddress': git.gitAddress, 'star': git.star, 'forks': git.forks,'openIssue':git.openIssue,
             'contributors': git.contributors, 'lastCommit': str(git.lastCommit), 'weekCommit': git.weekCommit,
             'monthCommit': git.monthCommit, 'seasonCommit': git.seasonCommit, 'releases': git.releases,
             'currentPriceCNY':float(price.currentPriceCNY),'currentPriceUSD':float(price.currentPriceUSD),
             'marketPriceCNY': float(price.marketPriceCNY),'marketPriceUSD':float(price.marketPriceUSD),
             'amount':price.amount,'supply':price.supply}

        return res




class ProjectAdd(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        content = {'name': args['name'],
                   'fullname': args['fullname'],
                   'gitAddress': args['gitAddress'],
                   'website': args['website'],
                   'whitepaper': args['whitepaper'],
                   'desp': args['desp']
                   }
        try:
            base = BlockProjectBase(name=content['name'], fullName=content['fullname'], website=content['website'],
                                    whitepaper=content['whitepaper'], desp=content['desp'])
            git = BlockProjectGit(name=base.name, gitAddress=content['gitAddress'])
            price = BlockProjectPrice(name=base.name)
            db.session.add(base)
            db.session.add(git)
            db.session.add(price)
            db.session.commit()
            return {'success': 1}
        except Exception as e:
            return {'success':0,'error':e}


class Test(Resource):
    def get(self):
        print("in Test get method....")
        for base,git,price in db.session.query(BlockProjectBase, BlockProjectGit,BlockProjectPrice).\
                                                filter(BlockProjectBase.name == BlockProjectGit.name).\
                                                filter(BlockProjectBase.name== BlockProjectPrice.name).all():
            print(base.fullName)
            print(git.gitAddress)
            print(price.amount)

        return {'text':'hello'}

    def post(self):
        args = parser.parse_args()
        print(args)
        content = {'name': args['name'],
                   'fullname':args['fullname'],
                   'gitAddress':args['gitAddress'],
                   'website':args['website'],
                   'whitepaper':args['whitepaper'],
                   'desp':args['desp']
                   }
        base=BlockProjectBase(name=content['name'],fullName=content['fullname'],website=content['website'],
                              whitepaper=content['whitepaper'],desp=content['desp'])
        git=BlockProjectGit(name=base.name,gitAddress=content['gitAddress'])
        price = BlockProjectPrice( name=base.name)
        db.session.add(base)
        db.session.add(git)
        db.session.add(price)
        db.session.commit()

        return {'status':'ok'}



api.add_resource(Test, '/test/')
api.add_resource(ProjectList, '/project/all/')
api.add_resource(ProjectDetail, '/project/<coinname>/')
api.add_resource(ProjectAdd, '/project/add/')