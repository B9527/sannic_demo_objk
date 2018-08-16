#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/10/18 4:48 PM
# @Author  : bai yang
# @Site    : 
# @File    : settings.py
# @Software: PyCharm

from sanic import Sanic
from sanic_mongo import Mongo
from sanic_cors import CORS
import sys

baseDir = sys.path[0] + '/image/'
imge_url = "http://192.168.1.63:8000/api/v1/first_page"


app = Sanic(__name__)
CORS(app, automatic_options=True)

mongo_uri = "mongodb://{host}:{port}/{database}".format(
    database='test',
    port=27017,
    host='localhost'
)  # type: str

Mongo.SetConfig(app, test=mongo_uri)
Mongo(app)
