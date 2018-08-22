#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/21/18 2:43 PM
# @Author  : bai yang
# @Site    : 
# @File    : comment_service.py
# @Software: PyCharm

from utils.article_exception import ArticleException


class CommentService(object):

    @staticmethod
    def params_check(params):
        valid_obj = {
            "create_time": "2018-08-21",
            "up_comment_id": None,
            "praise_num": 0,
            "image_url_list": []
        }

        if "image_url_list" in params.keys():
            params['image_url_list'] = params['image_url_list']

        if "up_comment_id" in params.keys():
            params['up_comment_id'] = params['up_comment_id']

        if "status" in params.keys():
            valid_obj['status'] = params['status']
        else:
            raise ArticleException("500", "缺少参数status")

        if "article_id" in params.keys():
            valid_obj['article_id'] = params['article_id']
        else:
            raise ArticleException("500", "缺少参数article_id")

        if "commenter_id" in params.keys():
            valid_obj['commenter_id'] = params['commenter_id']
        else:
            raise ArticleException("500", "缺少参数commenter_id")

        if "content" in params.keys():
            valid_obj['content'] = params['content']
        else:
            raise ArticleException("500", "缺少参数content")

        return valid_obj
