#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/10/18 4:29 PM
# @Author  : bai yang
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from .first_page_view import first_page_bp
from .first_page_view import ContentListView
from .upload_view import UploadImageView
from article.settings import baseDir

first_page_bp.add_route(ContentListView.as_view(), '/content')
first_page_bp.add_route(UploadImageView.as_view(), '/upImage')
first_page_bp.static('/image', baseDir)
__all__ = ['first_page_bp']

/home/yang/CODE/sanic_project/fw_project/image/61/2f9a705de9fe4c502b793e21e11c5d.jpg