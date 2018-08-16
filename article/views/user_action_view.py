#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/18 10:36 AM
# @Author  : bai yang
# @Site    : 
# @File    : user_action_view.py
# @Software: PyCharm

from sanic.views import HTTPMethodView
from article.service.user_action_service import UserActionService


class UserActionViews(HTTPMethodView):

    async def post(self, request):
        request_data = request.json
        operator = request.user
        if "action_type" in request_data.keys():
            action_type = request_data['action_type']
            user_action_service = UserActionService()
            user_action_service.do_user_action(action_type, operator, request_data)

