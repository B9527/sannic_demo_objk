#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/18 2:25 PM
# @Author  : bai yang
# @Site    : 
# @File    : user_action_service.py
# @Software: PyCharm


from article.models.concern_model import ConcernModel
from article.settings import app, db_name


class UserActionService(object):
    action_map = {
        "1": "关注",
        "-1": "取关",
        "2": "点赞",
        "-2": "取消点赞",
        "0": "阅读",
        "3": "转发",
        "4": "品论",
        "5": "收藏",
        "-5": "取消收藏",
        "6": "举报"
    }

    @staticmethod
    def concern_someone(operator, action_args):
        """
        关注
        :return:
        """
        concern_collection = app.mongo[db_name].follow_doc
        concern_model = ConcernModel(concern_collection)
        valid_obj = {
            "concern_person_id": operator,
            "concerned_person_id": action_args['concerned_person_id'],
            "create_time": "2018-08-17",
            "is_concern": "1"
        }
        concern_model.find_or_insert(valid_obj)

    @staticmethod
    def dis_concern_someone(operator, action_args):
        """
        取关
        :return:
        """
        pass

    @staticmethod
    def thumb_article(operator, action_args):
        """
        点赞
        :return:
        """
        pass

    @staticmethod
    def dis_thumb_article(operator, action_args):
        """
        取消点赞
        :return:
        """
        pass

    @staticmethod
    def read_article(operator, action_args):
        """
        阅读
        :return:
        """
        pass

    @staticmethod
    def forward_article(operator, action_args):
        """
        转发
        :return:
        """
        pass

    @staticmethod
    def comment_article(operator, action_args):
        """
        品论
        :return:
        """
        pass

    @staticmethod
    def collection_article(operator, action_args):
        """
        收藏
        :param operator:
        :param action_args:
        :return:
        """
        pass

    @staticmethod
    def dis_collection_article(operator, action_args):
        """

        :param operator:
        :param action_args:
        :return:
        """
        pass

    @staticmethod
    def report_article(operator, action_args):
        """

        :param operator:
        :param action_args:
        :return:
        """
        pass

    @classmethod
    def do_user_action(cls, action_type, operator, action_args):
        """
        取消收藏
        :param action_type: string
        :param operator: string
        :param action_args: dict
        :return:
        """
        if action_type == "1":
            cls.concern_someone(operator, action_args)
        elif action_type == "-1":
            cls.dis_concern_someone(operator, action_args)
        elif action_type == "2":
            cls.thumb_article(operator, action_args)
        elif action_type == "-2":
            cls.dis_thumb_article(operator, action_args)
        elif action_type == "0":
            cls.read_article(operator, action_args)
        elif action_type == "3":
            cls.forward_article(operator, action_args)
        elif action_type == "4":
            cls.comment_article(operator, action_args)
        elif action_type == "5":
            cls.collection_article(operator, action_args)
        elif action_type == "-5":
            cls.dis_collection_article(operator, action_args)
        elif action_type == "6":
            cls.report_article(operator, action_args)
        else:
            raise Exception("400", "can shu cuo wu")
