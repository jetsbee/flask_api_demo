import datetime as dt

from passlib.hash import pbkdf2_sha256 as sha256
from bson.objectid import ObjectId


class UserModel(object):
    ACCESS = {
        'guest': 0,
        'user': 1,
        'admin': 2,
    }

    def __init__(self, username, password, access=ACCESS['user'], **kwargs):
        self.username = username
        self.password = password
        self.access = access

        if kwargs.get('_id'):
            kwargs['_id'] = ObjectId(kwargs['_id'])
        if not kwargs.get('created_at'):
            kwargs['created_at'] = dt.datetime.now()

        self.__dict__.update((key, value) for key, value in kwargs.items())

    def allowed(self, access_level):
        return self.access >= access_level

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hashed_password):
        return sha256.verify(password, hashed_password)
