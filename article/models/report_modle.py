#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/18 8:11 PM
# @Author  : bai yang
# @Site    : 
# @File    : report_modle.py
# @Software: PyCharm


from __future__ import print_function
from __future__ import unicode_literals

from utils.mongodb import MongoDBModel


class ReportModel(MongoDBModel):
    """
    举报
    reporter_id: 举报人id
    article_id: 文章id or comment_id
    create_time: 创建时间
    content:评论类容
    type:类别 品论 or 文章
    """

    coll_name = "report_doc"

    fields = ["reporter_id", "article_id", "create_time", "content", "type"]