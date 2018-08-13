#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/10/18 4:30 PM
# @Author  : bai yang
# @Site    : 
# @File    : first_page_view.py
# @Software: PyCharm

from sanic.response import text, json
from sanic import Blueprint
from sanic.views import HTTPMethodView
from article.settings import app
from article.models.article_model import ArticleModel

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
        return text(return_data)

    async def post(self, request):
        request_data = request.json
        document = {
            "title": "hahahah",
            "type": "1",
            "content": "运生很兽shou兽瘦兽瘦ya",
            "create_time": "2018-08-10",
            "read_num": 20,
            "praise_num": 14,
            "forward_num": 20,
            "comment_num": 3,
            "collection_numbe": 13,
            "reports_num": 15,
            "update_time": "2018-08-10",
            "status": "1",
            "image_url_list": [],
            "tag_list": []
        }

        doc = await app.mongo['test'].runoob.insert_one(document)

        return text(request_data)

    async def delete(self, request):
        request_data = request.args
        print("request_data:", request_data)
        id = request_data['id']
        doc = await app.mongo['test'].runoob.remove_one()
        return json(request_data)


first_page_bp.add_route(ContentListView.as_view(), '/content')
