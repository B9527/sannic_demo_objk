#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/18 10:36 AM
# @Author  : bai yang
# @Site    : 
# @File    : user_action_view.py
# @Software: PyCharm

from sanic.views import HTTPMethodView
from sanic.response import json
from article.service.user_action_service import UserActionService


class UserActionViews(HTTPMethodView):

    async def get(self, request):
        return json(
            {
                "code": "200",
                "message": "success",
                "results": {}
            }
        )

    async def post(self, request):
        request_data = request.json

        return_data = {"code": "200",
                       "message": "success",
                       "results": {}
                       }
        # operator = request.user.id
        operator = "001"
        if "action_type" in request_data.keys():
            action_type = request_data['action_type']
            user_action_service = UserActionService()
            doc = await user_action_service.do_user_action(action_type, operator, request_data)
            return_data['results']['data'] = doc
            return json(return_data)
