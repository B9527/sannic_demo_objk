#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/15/18 2:20 PM
# @Author  : bai yang
# @Site    : 
# @File    : article_service.py
# @Software: PyCharm


class ArticlePostService(object):

    @staticmethod
    def add_default_data(data):
        data['creator'] = {
            "name": "陈运生",
            "id": "自己猜"
        }
        data['red_count'] = 0
        data['reports_num'] = 0
        data['thumbs_count'] = 0
        data['comment_count'] = 0
        data['collection_number'] = 0
        data['forward_num'] = 0
        data['create_time'] = '2018-08-15'
        data['update_time'] = '2018-08-15'
        return data