#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/10/18 5:59 PM
# @Author  : bai yang
# @Site    : 
# @File    : article_model.py
# @Software: PyCharm

from __future__ import print_function
from __future__ import unicode_literals

from utils.mongodb import MongoDBModel


class ArticleModel(MongoDBModel):
    """
    id:id
    title:标题
    content:内容
    type:类型   //0：短文  1： 长文
    create_time:创建时间
    creator_id:创建id
    update_time: 修改时间
    red_count:阅读数
    thumbs_count:点赞数
    forward_num: 转发数
    tag_list: 文章标签
    comment_count:品论数
    collection_number:收藏数
    reports_num:举报数
    status:'状态'， // 0: 草稿箱  1：已发布， -1：已删除, 2审核中
    image_url_list:图片列表
    is_read:是否读，
    is_thumb:是否点赞，
    is_comment:是否品论，
    is_forward:是否转发
    id_delete:
    """
    coll_name = "article_doc"
    fields = ['title', 'content', 'type', 'create_time', 'red_count', 'thumbs_count', 'forward_num', 'tag_list',
              'comment_count', 'creator', 'memo', 'is_delete', 'creator_id',
              'collection_number', 'reports_num', 'update_time', 'status', 'image_url_list'
              ]

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

    @staticmethod
    def tans_future_json():
        pass

    def find_title_or_content(self, key_words=""):
        """
        标题或者内容包含关键词
        :param key_words:
        :return:
        """
        docs = self.collection.find(
            {'$or':
                 [{'title': {'$regex': key_words}, 'type': '1', 'is_delete': '0'},
                  {"content": {'$regex': key_words}, "type": "0", 'is_delete': '0'}
                  ]
             }

        ).to_list(length=100)
        return docs
