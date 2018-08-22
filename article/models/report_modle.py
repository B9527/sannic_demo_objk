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
    status:
    """

    coll_name = "report_doc"

    fields = ["reporter_id", "article_id", "create_time", "content", "type"]

    async def find_or_insert(self, valid_obj):
        count_docs = await self.collection.count_documents({"reporter_id": valid_obj["reporter_id"],
                                                            "article_id": valid_obj[
                                                                'article_id']})

        if count_docs == 0:
            doc = self.collection.insert_one(valid_obj)
        else:
            doc = await self.collection.update_one({"reporter_id": valid_obj["reporter_id"],
                                                    "article_id": valid_obj[
                                                        'article_id']},
                                                   {'$set': valid_obj
                                                    }
                                                   )

        doc = await self.collection.find_one({"reporter_id": valid_obj["reporter_id"],
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