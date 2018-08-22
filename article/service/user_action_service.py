#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/18 2:25 PM
# @Author  : bai yang
# @Site    : 
# @File    : user_action_service.py
# @Software: PyCharm


from article.models.concern_model import ConcernModel
from article.models.thumb_model import ThumbModel
from article.models.follow_model import ForwardModel
from article.models.comment_model import CommentModel
from article.models.collect_model import CollectModel
from article.models.report_modle import ReportModel
from article.settings import app, db_name


class UserActionService(object):
    action_map = {
        "1": "关注",
        "-1": "取关",
        "2": "点赞",
        "-2": "取消点赞",
        "0": "阅读",
        "3": "删除转发",
        "-3": "转发",
        "4": "品论",
        "5": "收藏",
        "-5": "取消收藏",
        "6": "举报",
        "7": "搜索",
        "8": "刷新",
        "9": "发布",
        "10": "删除",
        "11": "草稿箱",
    }

    @staticmethod
    async def concern_someone(operator, action_args):
        """
        关注is_concern="1" else ="0"
        :return:
        """
        concern_collection = app.mongo[db_name].concern_doc
        concern_model = ConcernModel(concern_collection)
        valid_obj = {
            "concern_person_id": operator,
            "concerned_person_id": action_args['concerned_person_id'],
            "create_time": "2018-08-17",
            "is_concern": action_args['is_concern']
        }
        doc = await concern_model.find_or_insert(valid_obj)
        return doc

    # @staticmethod
    # async def dis_concern_someone(operator, action_args):
    #     """
    #     取关
    #     :return:
    #     """
    #     concern_collection = app.mongo[db_name].follow_doc
    #     concern_model = ConcernModel(concern_collection)
    #     valid_obj = {
    #         "concern_person_id": operator,
    #         "concerned_person_id": action_args['concerned_person_id'],
    #         "create_time": "2018-08-17",
    #         "is_concern": action_args['is_concern']
    #     }
    #     doc = await concern_model.find_or_insert(valid_obj)
    #     return doc

    @staticmethod
    async def thumb_article(operator, action_args):
        """
        点赞
        :return:
        """
        thumb_collection = app.mongo[db_name].thumb_doc
        thumb_model = ThumbModel(thumb_collection)
        valid_obj = {
            "praise_person_id": operator,
            "article_id": action_args['article_id'],
            "create_time": "2018-08-17",
            "is_praise": action_args['is_praise']
        }
        doc = await thumb_model.find_or_insert(valid_obj)
        return doc

    # @staticmethod
    # def dis_thumb_article(operator, action_args):
    #     """
    #     取消点赞
    #     :return:
    #     """
    #     thumb_collection = app.mongo[db_name].thumb_doc
    #     thumb_model = ThumbModel(thumb_collection)
    #     valid_obj = {
    #         "praise_person_id": operator,
    #         "article_id": action_args['article_id'],
    #         "create_time": "2018-08-17",
    #         "is_praise": "0"
    #     }
    #     thumb_model.find_or_insert(valid_obj)

    @staticmethod
    def read_article(operator, action_args):
        """
        阅读
        :return:
        """
        pass

    @staticmethod
    async def forward_article(operator, action_args):
        """
        转发
        :return:
        """
        forward_collection = app.mongo[db_name].forward_doc
        forward_model = ForwardModel(forward_collection)
        valid_obj = {
            "forward_person_id": operator,
            "article_id": action_args['article_id'],
            "create_time": "2018-08-17",
            "is_delete": action_args['is_delete']
        }
        doc = await forward_model.find_or_insert(valid_obj)
        return doc

    @staticmethod
    def comment_article(operator, action_args):
        """
        品论
        :return:
        """
        comment_collection = app.mongo[db_name].comment_doc
        comment_model = CommentModel(comment_collection)
        valid_obj = {
            "commenter_id": operator,
            "article_id": action_args['article_id'],
            "create_time": "2018-08-17",
            "up_comment_id": None,
            "content": "",
            "image_url_list": [],
            "praise_num": 0,
            "status": "0"
        }
        # comment_model.find_or_insert(valid_obj)

    @staticmethod
    async def collection_article(operator, action_args):
        """
        收藏
        :param operator:
        :param action_args:
        :return:
        """
        collect_collection = app.mongo[db_name].collect_doc
        collect_model = CollectModel(collect_collection)
        valid_obj = {
            "collector_id": operator,
            "article_id": action_args['article_id'],
            "create_time": "2018-08-17",
            "is_collect": action_args['is_collect']
        }
        doc = await collect_model.find_or_insert(valid_obj)
        return doc

    @staticmethod
    def dis_collection_article(operator, action_args):
        """
        取消收藏
        :param operator:
        :param action_args:
        :return:
        """
        collect_collection = app.mongo[db_name].collect_doc
        collect_model = CollectModel(collect_collection)
        valid_obj = {
            "collector_id": operator,
            "article_id": action_args['article_id'],
            "create_time": "2018-08-17",
            "is_collect": '0'
        }
        collect_model.find_or_insert(valid_obj)

    @staticmethod
    async def report_article(operator, action_args):
        """
        举报
        :param operator:
        :param action_args:
        :return:
        """
        report_collection = app.mongo[db_name].report_doc
        report_model = ReportModel(report_collection)
        valid_obj = {
            "reporter_id": operator,
            "article_id": action_args['article_id'],
            "create_time": "2018-08-17",
            "content": action_args['content'],
            "type": action_args['type'],
            "status": action_args['status']
        }
        doc = await report_model.find_or_insert(valid_obj)
        return doc

    @classmethod
    async def do_user_action(cls, action_type, operator, action_args):
        """
        :param action_type: string
        :param operator: string
        :param action_args: dict
        :return:
        """
        if action_type == "1":
            action_args['is_concern'] = "1"
            doc = await cls.concern_someone(operator, action_args)
            return doc
        elif action_type == "-1":
            action_args['is_concern'] = "0"
            doc = await cls.concern_someone(operator, action_args)
            return doc
        elif action_type == "2":
            action_args['is_praise'] = "1"
            doc = await cls.thumb_article(operator, action_args)
            return doc
        elif action_type == "-2":
            action_args['is_praise'] = "0"
            doc = await cls.thumb_article(operator, action_args)
            return doc
        elif action_type == "0":
            # cls.read_article(operator, action_args)
            pass
        elif action_type == "3":
            action_args['is_forward'] = "1"
            doc = await cls.forward_article(operator, action_args)
            return doc
        elif action_type == "-3":
            action_args['is_forward'] = "0"
            doc = await cls.forward_article(operator, action_args)
            return doc
        elif action_type == "4":
            cls.comment_article(operator, action_args)
        elif action_type == "5":
            action_args['is_collect'] = "1"
            doc = await cls.collection_article(operator, action_args)
            return doc

        elif action_type == "-5":
            action_args['is_collect'] = "0"
            doc = await cls.collection_article(operator, action_args)
            return doc
        elif action_type == "6":
            action_args['status'] = "0"
            doc = await cls.report_article(operator, action_args)
            return doc
        else:
            raise Exception("400", "can shu cuo wu")
