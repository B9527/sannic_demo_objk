#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/18 7:47 PM
# @Author  : bai yang
# @Site    : 
# @File    : thumb_model.py
# @Software: PyCharm

from __future__ import print_function
from __future__ import unicode_literals

from utils.mongodb import MongoDBModel


class ThumbModel(MongoDBModel):
    """
    点赞
    concern_person_id: 点赞人id
    article_id: 文章id
    create_time: 创建时间
    is_praise: 是否点赞
    """

    coll_name = "thumb_doc"

    fields = ["praise_person_id", "article_id", "create_time", "is_praise"]