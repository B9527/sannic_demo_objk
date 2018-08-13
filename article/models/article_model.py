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
    coll_name = "runoob"
    fields = ['title', 'content', 'type', 'create_time', 'read_num', 'praise_num', 'forward_num', 'tag_list'
              'comment_num', 'collection_numbe', 'reports_num', 'update_time', 'status', 'image_url_list'
              ]
