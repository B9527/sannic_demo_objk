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
        count_docs = await self.collection.count_documents({"concern_person_id": valid_obj["concern_person_id"],
                                                            "concerned_person_id": valid_obj[
                                                                'concerned_person_id']})

        if count_docs == 0:
            doc = self.collection.insert_one(valid_obj)
        else:
            doc = await self.collection.update_one({"concern_person_id": valid_obj["concern_person_id"],
                                                    "concerned_person_id": valid_obj[
                                                        'concerned_person_id']}, {'$set': {'is_concern': '1'}})
        return doc
