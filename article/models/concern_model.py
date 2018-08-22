#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/17/18 9:57 AM
# @Author  : bai yang
# @Site    : 
# @File    : concern_model.py
# @Software: PyCharm


from __future__ import print_function
from __future__ import unicode_literals

from utils.mongodb import MongoDBModel
from bson import ObjectId


class ConcernModel(MongoDBModel):
    """
    关注
    concern_person: 关注人id
    concerned_person: 被关注人id
    create_time: 创建时间
    is_concern:是否关注
    """

    coll_name = "concern_doc"

    fields = ["concern_person_id", "concerned_person_id", "create_time", "is_concern"]

    async def find_or_insert(self, valid_obj):
        print("hello")
        count_docs = await self.collection.count_documents({"concern_person_id": valid_obj["concern_person_id"],
                                                            "concerned_person_id": valid_obj[
                                                                'concerned_person_id']})

        print("count_docs:", count_docs)
        print("valid_obj:", valid_obj)
        if count_docs == 0:

            doc = await self.collection.insert_one(valid_obj)
        else:
            doc = await self.collection.update_one({"concern_person_id": valid_obj["concern_person_id"],
                                                    "concerned_person_id": valid_obj[
                                                        'concerned_person_id']},
                                                   {'$set': {'is_concern': valid_obj['is_concern'],
                                                             'create_time': valid_obj['create_time']}})
        doc = await self.collection.find_one({"concern_person_id": valid_obj["concern_person_id"],
                                              "concerned_person_id": valid_obj[
                                                  'concerned_person_id']})
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
            return "gggggggg"

    async def check_is_concern(self, concern_person_id, concerned_person_id):
        count_docs = await self.collection.count_documents({"concern_person_id": concern_person_id,
                                                            "concerned_person_id": concerned_person_id,
                                                            "is_concern": "1"})
        if count_docs == 0:
            return False
        else:
            return True
