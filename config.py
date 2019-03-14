class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_URI = 'mongodb://db:27017/flask_api_demo'


class TestingConfig(Config):
    TESTING = True
    MONGO_URI = 'mongodb://db:27017/flask_api_demo_test'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass
