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

    fields = ["forward_person_id", "article_id", "create_time", "is_forward"]

    async def find_or_insert(self, valid_obj):
        count_docs = await self.collection.count_documents({"forward_person_id": valid_obj["forward_person_id"],
                                                            "article_id": valid_obj[
                                                                'article_id']})

        if count_docs == 0:

            doc = await self.collection.insert_one(valid_obj)

        else:
            doc = await self.collection.update_one({"forward_person_id": valid_obj["forward_person_id"],
                                                    "article_id": valid_obj[
                                                        'article_id']},
                                                   {'$set': {'is_forward': valid_obj['is_forward'],
                                                             'create_time': valid_obj['create_time']}})
        doc = await self.collection.find_one({"forward_person_id": valid_obj["forward_person_id"],
                                              "article_id": valid_obj[
                                                  'article_id']})

        return self.trans_obj_id_str(doc)

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
        else:
            raise Exception("500", "can shu cuo wu")
