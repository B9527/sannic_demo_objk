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
from aoiklivereload import LiveReloader

reloader = LiveReloader()
reloader.start_watcher_thread()

app = Sanic(__name__)
CORS(app, automatic_options=True)

mongo_uri = "mongodb://{host}:{port}/{database}".format(
    database='test',
    port=27017,
    host='localhost'
)

Mongo.SetConfig(app, test=mongo_uri)
Mongo(app)
