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

    async def find_or_insert(self, valid_obj):
        count_docs = await self.collection.count_documents({"collector_id": valid_obj["collector_id"],
                                                            "article_id": valid_obj[
                                                                'article_id']})

        if count_docs == 0:
            doc = self.collection.insert_one(valid_obj)
        else:
            print("is_collect:", valid_obj['is_collect'])
            doc = await self.collection.update_one({"collector_id": valid_obj["collector_id"],
                                                    "article_id": valid_obj[
                                                        'article_id']},
                                                   {'$set': {'is_collect': valid_obj['is_collect'],
                                                             'create_time': valid_obj['create_time']}})

        doc = await self.collection.find_one({"collector_id": valid_obj["collector_id"],
                                              "article_id": valid_obj[
                                                  'article_id']})

        doc = self.trans_obj_id_str(doc)
        return doc

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

    async def check_is_collect(self, collector_id, article_id):
        count_docs = await self.collection.count_documents({"collector_id": collector_id,
                                                            "article_id": article_id, "is_collect":'1'})
        if count_docs == 0:
            return False
        else:
            return True
