#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/10/18 4:30 PM
# @Author  : bai yang
# @Site    : 
# @File    : first_page_view.py
# @Software: PyCharm

from sanic.response import json
from sanic import Blueprint
from sanic.views import HTTPMethodView
from article.settings import app


# from playhouse.shortcuts import model_to_dict

first_page_bp = Blueprint('first_page', url_prefix='/api/first_page')


class ContentListView(HTTPMethodView):

    async def get(self, request):
        return_data = {
            "error_message": "success",
            "error_code": "0",
            "results": {}
        }
        docs = await app.mongo['test'].runoob.find().to_list(length=100)
        for doc in docs:
            doc['id'] = str(doc['_id'])
            del doc['_id']
        return_data['results']['data'] = docs
        return json(return_data)


first_page_bp.add_route(ContentListView.as_view(), '/content')

