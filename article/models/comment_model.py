#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/18 8:06 PM
# @Author  : bai yang
# @Site    : 
# @File    : comment_model.py
# @Software: PyCharm

from __future__ import print_function
from __future__ import unicode_literals

from utils.mongodb import MongoDBModel


class CommentModel(MongoDBModel):
    """
    评论
    commenter_id: 评论人id
    article_id: 文章id
    create_time: 创建时间
    up_comment_id: 上级评论  // 默认未None或者其他
    content:评论类容
    image_url_list:图片列表
    praise_num:点赞数
    status:状态  // 0: 草稿箱  1：已发布， -1：已删除
    """

    coll_name = "comment_doc"

    fields = ["commenter_id", "article_id", "create_time", "up_comment_id", "content", "image_url_list",
              'praise_num', "status"]

    @staticmethod
    def trans_obj_id_str(docs):

        if isinstance(docs, list):
            for doc in docs:
                doc_id = str(doc.pop("_id"))
                doc['id'] = doc_id
            return docs
        elif isinstance(docs, dict):
            doc_id = str(docs.pop('_id'))
            docs['id'] = doc_id
            return docs




