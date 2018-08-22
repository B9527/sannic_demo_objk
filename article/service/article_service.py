#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/15/18 2:20 PM
# @Author  : bai yang
# @Site    : 
# @File    : article_service.py
# @Software: PyCharm

from article.settings import app, db_name
from article.models.concern_model import ConcernModel
from article.models.collect_model import CollectModel
from article.models.comment_model import CommentModel


class ArticlePostService(object):

    @staticmethod
    def add_default_data(data):
        data['creator'] = {
            "name": "陈运生",
            "id": "自己猜",
            "image_url": "http://192.168.1.63:8000/api/v1/first_page/image/61/2f9a705de9fe4c502b793e21e11c5d.jpg",
        }
        data['creator_id'] = "自己猜"
        data['red_count'] = 0
        data['reports_num'] = 0
        data['thumbs_count'] = 0
        data['comment_count'] = 0
        data['collection_number'] = 0
        data['forward_num'] = 0
        data['create_time'] = '2018-08-15'
        data['update_time'] = '2018-08-15'
        return data


class ArticleCommonService(object):

    @staticmethod
    def check_article_is_concern(concern_person_id, concerned_person_id):
        """
        检测用户是否关注该文章
        :return:
        """
        print("concern_person_id:", concern_person_id)
        print("concerned_person_id:", concerned_person_id)
        concern_collection = app.mongo[db_name].concern_doc
        concern_model = ConcernModel(concern_collection)
        return concern_model.check_is_concern(concern_person_id, concerned_person_id)

    @staticmethod
    def check_article_is_collect(collector_id, article_id):
        """
        检测用户是否搜藏该文章
        :return:
        """
        print("collector_id:", collector_id)
        print("article_id:", article_id)
        collect_collection = app.mongo[db_name].collect_doc
        collect_model = CollectModel(collect_collection)
        return collect_model.check_is_collect(collector_id, article_id)

    @staticmethod
    async def get_comment_by_article_id(article_id):
        """
        根据文章id获取评论
        :param article_id:
        :return:
        """
        print("article_id:", article_id)
        comment_collection = app.mongo[db_name].comment_doc
        comment_model = CommentModel(comment_collection)
        comment_docs = await comment_model.find_by_obj({"article_id": article_id})
        return comment_model.trans_obj_id_str(comment_docs)
