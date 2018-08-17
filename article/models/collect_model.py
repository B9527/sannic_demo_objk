#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/18 7:58 PM
# @Author  : bai yang
# @Site    : 
# @File    : collect_model.py
# @Software: PyCharm


from __future__ import print_function
from __future__ import unicode_literals

from utils.mongodb import MongoDBModel


class CollectModel(MongoDBModel):
    """

    collector_id: 收藏人id
    article_id: 文章id
    create_time: 创建时间
    is_collect:是否收藏
    """

    coll_name = "collect_doc"

    fields = ["collector_id", "article_id", "create_time", "is_collect"]