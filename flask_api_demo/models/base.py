from .db import mongo


class Collection(object):
    users = mongo.db.users
    revoked_tokens = mongo.db.revoked_tokens


class ModelController(object):
    def __init__(self, model_type):
        assert model_type in ['users', 'revoked_tokens'], 'Invalid model_type.'

        self.collection = getattr(Collection, model_type)
        self.set_model(model_type)

    def set_model(self, m):
        if m in ['users']:
            class_map = {
                'users': 'UserModel',
            }
            module = __import__('user', globals=globals(), level=1)
            self.__dict__['model_class_'] = getattr(module, class_map[m])
        elif m is 'revoked_tokens':
            class_map = {
                'revoked_tokens': 'RevokedTokenModel',
            }
            module = __import__('token', globals=globals(), level=1)
            self.__dict__['model_class_'] = getattr(module, class_map[m])

    def create(self, model_obj):
        return self.collection.insert_one(model_obj.__dict__).inserted_id

    def read_all(self):
        docs = self.collection.find({})

        return [self.model_class_(**doc) for doc in docs]

    def read_one(self, filter_q):
        doc = self.collection.find_one(filter_q)

        return self.model_class_(**doc) if doc else None

    def find_one_and_modify(self, filter_q, field):
        return self.collection.update_one(filter_q, {'$set': field}).modified_count
