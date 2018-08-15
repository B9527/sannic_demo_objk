#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/15/18 4:51 PM
# @Author  : bai yang
# @Site    : 
# @File    : upload_view.py
# @Software: PyCharm
import hashlib
import os
from sanic.response import json
from sanic.views import HTTPMethodView
from article.settings import baseDir, imge_url


# 获取图片后缀名
def get_suffix(filename):
    temp_addr = filename.split('.')
    suffix = temp_addr[-1]
    file_type = ['jpg', 'jpeg', 'gif', 'png']
    if len(temp_addr) < 2:
        return 'error name'
    elif suffix not in file_type:
        return 'error type'
    else:
        return suffix


class UploadImageView(HTTPMethodView):
    """
         上传图片文件接口
    """

    async def get(self, request):
        return_data = {
            "message": "",
            "code": "200",
            "results": {}
        }
        return json(return_data)

    async def post(self, request):

        return_data = {
            "message": "",
            "code": "200",
            "results": {}
        }

        image = request.files.get('file').body
        # 判断文件是否支持
        image_name = request.files.get('file').name
        image_suffix = get_suffix(image_name)
        if 'error' in image_suffix:
            return_data['code'] = "300"
            return_data['message'] = "图片不支持"
            return json(return_data)
        # 组织图片存储路径
        m1 = hashlib.md5()
        m1.update(image)
        md5_name = m1.hexdigest()

        # 用 md5 的前两位来建文件夹，防止单个文件夹下图片过多，又或者根目录下建立太多的文件夹
        save_dir = baseDir + md5_name[0:2] + '/'
        save_path = save_dir + md5_name[2:] + '.' + image_suffix
        res_path = '/' + md5_name[0:2] + '/' + md5_name[2:] + '.' + image_suffix

        # 如果文件夹不存在，就创建文件夹
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # 将文件写入到硬盘
        temp_file = open(save_path, 'wb')
        temp_file.write(image)
        temp_file.close()

        # 给客户端返回结果
        return_data['results']['path'] = imge_url + '/image'+res_path
        return json(return_data)



