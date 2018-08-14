#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/10/18 4:30 PM
# @Author  : bai yang
# @Site    : 
# @File    : first_page_view.py
# @Software: PyCharm

from sanic.response import text, json
from bson import ObjectId
from sanic import Blueprint
from sanic.views import HTTPMethodView
from article.settings import app
from article.models.article_model import ArticleModel

# from playhouse.shortcuts import model_to_dict

first_page_bp = Blueprint('first_page', url_prefix='/api/first_page')


class ContentListView(HTTPMethodView):

    def __init__(self):
        self.collection = app.mongo['test'].runoob

    async def get(self, request):
        return_data = {
            "error_message": "success",
            "error_code": "0",
            "results": {}
        }
        request_data = request.args
        doc_id = request_data['id']
        article_model = ArticleModel(self.collection)
        docs = await article_model.find()
        doc = await article_model.find_by_id(doc_id)
        doc = article_model.trans_obj_id_str(doc)
        docs = article_model.trans_obj_id_str(docs)
        return_data['results']['data'] = docs
        return json(return_data, status=200)

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
        article_model = ArticleModel(self.collection)
        result = await article_model.create(document)
        valid_obj = article_model.get_valid_obj(document)
        valid_obj['id'] = str(result.inserted_id)

        return json(valid_obj)

    async def delete(self, request):
        request_data = request.args
        print("request_data:", request_data)
        article_id = request_data['id'][0]
        article_model = ArticleModel(self.collection)
        article_model.remove_by_id(article_id)
        return json(request_data)

    async def put(self, request):
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
        request_data = request.json
        doc_id = request_data['id']
        article_model = ArticleModel(self.collection)
        new_doc = await article_model.update_by_id(doc_id, request_data)
        new_doc = article_model.trans_obj_id_str(new_doc)
        print("request_data:", new_doc)
        return json(new_doc)


first_page_bp.add_route(ContentListView.as_view(), '/content')
