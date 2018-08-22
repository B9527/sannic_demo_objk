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

    async def find_or_insert(self, valid_obj):
        count_docs = await self.collection.count_documents({"praise_person_id": valid_obj["praise_person_id"],
                                                            "article_id": valid_obj[
                                                                'article_id']})

        if count_docs == 0:
            doc = self.collection.insert_one(valid_obj)
        else:
            doc = await self.collection.update_one({"praise_person_id": valid_obj["praise_person_id"],
                                                    "article_id": valid_obj[
                                                        'article_id']},
                                                   {'$set': {'is_praise': valid_obj['is_praise'],
                                                             'create_time': valid_obj['create_time']}})

        doc = await self.collection.find_one({"praise_person_id": valid_obj["praise_person_id"],
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
            return "gggggggg"
