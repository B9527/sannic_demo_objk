#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/10/18 4:30 PM
# @Author  : bai yang
# @Site    : 
# @File    : first_page_view.py
# @Software: PyCharm

from sanic.response import json, text
from sanic import Blueprint
from sanic.views import HTTPMethodView
from article.settings import app, db_name
from article.models.article_model import ArticleModel
from article.service.article_service import ArticlePostService

# from playhouse.shortcuts import model_to_dict

first_page_bp = Blueprint('first_page', url_prefix='/api/v1/first_page')


class ContentListView(HTTPMethodView):

    def __init__(self):
        self.collection = app.mongo[db_name].article_doc

    async def get(self, request):
        return_data = {
            "message": "",
            "code": "200",
            "results": {}
        }
        try:
            print(app.mongo)
            request_data = request.args
            article_model = ArticleModel(self.collection)
            # article_model = ArticleModel("article_doc")
            filter_args = {
                'is_delete': '0'
            }
            if "key_words" in request_data.keys():
                key_words = request_data['key_words'][0]
                docs = await article_model.find_title_or_content(key_words)
                count = len(docs)
            else:
                if "id" in request_data.keys():
                    print("id:", request_data['id'][0])
                    docs = await article_model.find_by_id(request_data['id'][0])
                    print("docs:", docs)
                    count = 1
                else:
                    if "creator_id" in request_data.keys():
                        filter_args['creator_id'] = request_data['creator_id'][0]
                    print("filter_args:", filter_args)
                    docs = await article_model.find_by_obj(filter_args)
                    ###
                    count = await self.collection.count_documents(filter_args)
            ###
            docs = article_model.trans_obj_id_str(docs)
            if isinstance(docs, dict):
                temp_list = [docs]
                docs = temp_list
            return_data['results']['data_list'] = docs
            return_data['results']['count'] = count
        except Exception as ex:
            return_data['results']['data_list'] = []
            return_data['results']['count'] = 0
            return_data['message'] = str(ex)
            return_data['code'] = '500'
        finally:
            return json(return_data, status=200)

    async def post(self, request):

        return_data = {
            "message": "",
            "code": "200",
            "results": {}
        }
        request_data = request.json
        try:
            doc_data = ArticlePostService.add_default_data(request_data)

            article_model = ArticleModel(self.collection)
            valid_obj = article_model.get_valid_obj(doc_data)
            valid_obj['is_delete'] = '0'
            result = await article_model.create(valid_obj)
            valid_obj = article_model.trans_obj_id_str(valid_obj)
            return_data['results']['data'] = valid_obj
        except Exception as ex:
            return_data['message'] = str(ex)
            return_data['code'] = '500'
            return_data['results']['data'] = request_data
        finally:
            return json(return_data)

    async def delete(self, request):

        return_data = {
            "message": "删除成功",
            "code": "200",
            "results": {}
        }
        try:
            request_data = request.args
            if "id" in request_data.keys():
                article_id = request_data['id'][0]
                article_model = ArticleModel(self.collection)
                article_model.remove_by_id(article_id)
                return json(return_data)
            else:
                return_data = {
                    "message": "缺少参数id",
                    "code": "300",
                    "results": {}
                }
                return json(return_data)
        except Exception as e:
            return_data = {
                "message": str(e),
                "code": "500",
                "results": {}
            }
            return json(return_data)

    async def put(self, request):

        return_data = {
            "message": "修改成功",
            "code": "200",
            "results": {}
        }
        request_data = request.json
        try:
            doc_id = request_data['id']
            article_model = ArticleModel(self.collection)
            new_doc = await article_model.update_by_id(doc_id, request_data)
            new_doc = article_model.trans_obj_id_str(new_doc)
            return_data['results']['data'] = new_doc
        except Exception as ex:
            return_data['results']['data'] = request_data
            return_data['code'] = '500'
            return_data['message'] = str(ex)
        finally:
            return json(return_data)
