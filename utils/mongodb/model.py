from __future__ import print_function
from __future__ import unicode_literals

from bson import ObjectId
from utils.basic.model import Model


class MongoDBModel(Model):
    coll_name = None
    fields = None

    def __init__(self, collection):
        self.collection = collection
        self.on_init()

    def on_init(self):
        pass

    @staticmethod
    def __transform_doc(doc):
        doc['_id'] = str(doc['_id'])
        return doc

    def get_valid_obj(self, obj):
        # check fields
        valid_obj = {}

        if not self.fields:
            valid_obj = obj.copy()
        else:
            for f in self.fields:
                if f in obj.keys():
                    valid_obj[f] = obj[f]
                else:
                    valid_obj[f] = None
        return valid_obj

    def find(self):
        docs = self.collection.find().to_list(length=100)
        return docs

    def find_by_id(self, id):
        doc = self.collection.find_one({'_id': ObjectId(id)})
        return None if doc is None else doc

    def create(self, obj):
        # valid_obj = self.get_valid_obj(obj)
        result = self.collection.insert_one(obj)
        return result

    def update_by_id(self, id, obj):
        # doc = self.find_by_id(id)
        # if doc is None:
        #     return None

        # valid_obj = self.get_valid_obj(obj)
        self.collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': obj}
        )
        doc = self.find_by_id(id)
        if doc is None:
            return None
        return doc

    def remove_by_id(self, id):
        doc = self.find_by_id(id)
        if doc is None:
            return False
        else:
            self.collection.delete_one({'_id': ObjectId(id)})
            return True
