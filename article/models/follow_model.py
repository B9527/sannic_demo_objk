#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/18 7:37 PM
# @Author  : bai yang
# @Site    : 
# @File    : follow_model.py
# @Software: PyCharm

from __future__ import print_function
from __future__ import unicode_literals

from utils.mongodb import MongoDBModel


class ForwardModel(MongoDBModel):
    """
    转发
    forward_person_id: 转发人id
    article_id: 文章id
    create_time: 创建时间
    is_delete:是否删除
    """

    coll_name = "forward_doc"

    fields = ["forward_person_id", "article_id", "create_time", "is_delete"]