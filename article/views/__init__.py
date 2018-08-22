#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/10/18 4:29 PM
# @Author  : bai yang
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from .first_page_view import first_page_bp
from .first_page_view import ContentListView
from .user_action_view import UserActionViews
from .upload_view import UploadImageView
from .comment_view import CommentView
from .article_detail_view import ArticleDetailView
from article.settings import baseDir

first_page_bp.add_route(ContentListView.as_view(), '/content')
first_page_bp.add_route(UploadImageView.as_view(), '/upImage')
first_page_bp.add_route(UserActionViews.as_view(), '/userAction')
first_page_bp.static('/image', baseDir)
first_page_bp.add_route(CommentView.as_view(), '/comment')
first_page_bp.add_route(ArticleDetailView.as_view(), '/article_detail')
__all__ = ['first_page_bp']

