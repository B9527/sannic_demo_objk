#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/22/18 11:14 AM
# @Author  : bai yang
# @Site    : 
# @File    : article_detail_view.py
# @Software: PyCharm

from sanic.response import json, text
from utils.article_exception import ArticleException
from sanic.views import HTTPMethodView
from article.settings import app, db_name
from article.models.article_model import ArticleModel
from article.service.article_service import ArticleCommonService


class ArticleDetailView(HTTPMethodView):

    def __init__(self):
        self.collection = app.mongo[db_name].article_doc

    async def get(self, request):
        return_data = {
            "message": "",
            "code": "200",
            "results": {}
        }

        try:
            request_data = request.args
            user_id = "001"
            article_model = ArticleModel(self.collection)
            if "id" in request_data.keys():
                article_id = request_data['id'][0]
                docs = await article_model.find_by_id(article_id)
                docs = article_model.trans_obj_id_str(docs)
                is_concern = await ArticleCommonService.check_article_is_concern(user_id, docs['creator_id'])
                is_collect = await ArticleCommonService.check_article_is_collect(user_id, docs['id'])
                comment_list = await ArticleCommonService.get_comment_by_article_id(docs['id'])
                return_data['results']['data'] = docs
                return_data['results']['data']['is_concern'] = is_concern
                return_data['results']['data']['is_collect'] = is_collect
                return_data['results']['comment_list'] = comment_list
            else:
                raise ArticleException('500', "缺少参数id")
        except ArticleException as ae:
            return_data['message'] = ae.error_message
            return_data['code'] = ae.error_code
        except Exception as e:
            return_data['message'] = str(e)
            return_data['code'] = '500'

        return json(return_data)
