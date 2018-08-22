#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/21/18 2:48 PM
# @Author  : bai yang
# @Site    : 
# @File    : article_exception.py
# @Software: PyCharm


class ArticleException(Exception):
    def __init__(self, error_code, error_message):
        self.error_code = error_code
        self.error_message = error_message
