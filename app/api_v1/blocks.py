#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/29 0:02
# @Author  : Vniex
# @Site    : 
# @File    : news.py
# @Software: PyCharm
import math
import simplejson as json
from flask_restful import Resource,reqparse

from app.models import BlockProjectBase,BlockProjectGit,BlockProjectPrice
from app.api_v1 import api
from app import db
from .Utils import parseIcon,price2float

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('fullname', type=str)
parser.add_argument('gitAddress', type=str)
parser.add_argument('website', type=str)
parser.add_argument('whitepaper', type=str)
parser.add_argument('desp', type=str)
parser.add_argument('iconSmall', type=str)
parser.add_argument('iconMid', type=str)
parser.add_argument('page', type=int)
parser.add_argument('per_page', type=int)


class ProjectList(Resource):
    def get(self):
        args = parser.parse_args()
        content = {'page': args['page'],'per_page':args['per_page']}
        res=[]
        querySuggest = []
        projectBase=db.session.query(BlockProjectBase).all()
        pages=math.ceil(len(projectBase)/content['per_page'])
        for base in projectBase:
            querySuggest.append({'val':base.name,'value':base.fullName+'('+base.name+')'})
        for base,git,price in db.session.query(BlockProjectBase, BlockProjectGit,BlockProjectPrice).\
                                                filter(BlockProjectBase.name == BlockProjectGit.name).\
                                                filter(BlockProjectBase.name== BlockProjectPrice.name).\
                                                order_by(db.desc(BlockProjectGit.lastCommit)).limit(content['per_page']).offset(content['per_page']*(content['page']-1)):
            res.append({'name':base.name,'gitAddress':git.gitAddress,'star':git.star,'forks':git.forks,'contributors':git.contributors,
                 'lastCommit':str(git.lastCommit),'weekCommit':git.weekCommit,'monthCommit':git.monthCommit,'seasonCommit':git.seasonCommit,
                 'watch':git.watch,'issue':git.openIssue,
                 'releases':git.releases,'currentPriceCNY':price2float(price.currentPriceCNY),'marketPriceCNY':price2float(price.marketPriceCNY),'iconSmall':base.iconSmall})
        return {'pages': pages,'res':res,'querySuggest':querySuggest}

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
             'currentPriceCNY':price2float(price.currentPriceCNY),'currentPriceUSD':price2float(price.currentPriceUSD),
             'marketPriceCNY': price2float(price.marketPriceCNY),'marketPriceUSD':price2float(price.marketPriceUSD),
             'amount':price.amount,'supply':price.supply,'iconMid':base.iconMid,'commitStats':git.commitStats}

        return res




class ProjectAdd(Resource):
    def post(self):
        args = parser.parse_args()
        content = {'name': args['name'],
                   'fullname': args['fullname'],
                   'gitAddress': args['gitAddress'],
                   'website': args['website'],
                   'whitepaper': args['whitepaper'],
                   'desp': args['desp'],
                   'iconSmall': args['iconSmall'],
                   'iconMid': args['iconMid']
                   }

        iconSmall=parseIcon("http:"+content['iconSmall'],saveName=content['name']+'_small')
        iconMid = parseIcon("http:"+content['iconMid'],saveName=content['name']+'_mid')
        try:
            base = BlockProjectBase(name=content['name'], fullName=content['fullname'], website=content['website'],
                                    whitepaper=content['whitepaper'], desp=content['desp'],iconSmall=iconSmall,iconMid=iconMid )
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
