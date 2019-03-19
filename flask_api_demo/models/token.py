import datetime as dt

from bson.objectid import ObjectId


class RevokedTokenModel(object):
    def __init__(self, jti, **kwargs):
        self.jti = jti

        if kwargs.get('_id'):
            kwargs['_id'] = ObjectId(kwargs['_id'])
        if not kwargs.get('created_at'):
            kwargs['created_at'] = dt.datetime.now()

        self.__dict__.update((key, value) for key, value in kwargs.items())
