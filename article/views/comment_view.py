#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/21/18 11:29 AM
# @Author  : bai yang
# @Site    : 
# @File    : comment_view.py
# @Software: PyCharm

from sanic.response import json, text
from sanic.views import HTTPMethodView
from article.settings import app, db_name
from article.models.comment_model import CommentModel
from article.service.comment_service import CommentService
from utils.article_exception import ArticleException


class CommentView(HTTPMethodView):
    """
    评论
    """

    def __init__(self):
        self.collection = app.mongo[db_name].comment_doc

    async def get(self, request):

        return_data = {
            "message": "",
            "code": "200",
            "results": {}
        }

        try:
            request_data = request.args
            comment_model = CommentModel(self.collection)
            filter_args = {
                'status': '1'
            }
            if "commenter_id" in request_data.keys():
                commenter_id = request_data['commenter_id'][0]
                filter_args['commenter_id'] = commenter_id
            if "article_id" in request_data.keys():
                article_id = request_data['article_id'][0]
                filter_args['article_id'] = article_id
            ###
            docs = await comment_model.find_by_obj(filter_args)
            count = await self.collection.count_documents(filter_args)
            print("count:", count)
            ###
            docs = comment_model.trans_obj_id_str(docs)
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
        # user_id = request.user.id
        request_user_id = "00000"
        code = '200'
        message = 'success'

        try:
            request_data = request.json
            request_data['commenter_id'] = request_user_id
            valid_obj = CommentService.params_check(request_data)
            comment_model = CommentModel(self.collection)
            comment_model.create(valid_obj)
        except ArticleException as ae:
            code = ae.error_code
            message = ae.error_message
        except Exception as e:
            code = "500"
            message = str(e)
        finally:
            return json(
                {
                    "code": code,
                    "message": message,
                    "results": {},
                    "request_user": request_user_id
                }
            )

    async def delete(self, request):

        code = '200'
        message = 'success'
        request_data = request.args
        try:
            if "id" in request_data.keys():
                id = request_data['id'][0]
                comment_model = CommentModel(self.collection)
                comment_model.update_by_id(id, {"status": "-1"})
            else:
                raise ArticleException('500', "缺少参数id")
        except ArticleException as ae:
            code = ae.error_code
            message = ae.error_message
        except Exception as e:
            code = "500"
            message = str(e)
        finally:
            return json(
                {
                    "code": code,
                    "message": message,
                    "results": {},
                }
            )
