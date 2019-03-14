from flask import Flask
from flask_restful import Api

import config


def create_app():
    app = Flask(__name__)

    if app.config['ENV'] == 'development':
        app.config.from_object(config.DevelopmentConfig)
    elif app.config['ENV'] == 'testing':
        app.config.from_object(config.TestingConfig)
    elif app.config['ENV'] == 'production':
        app.config.from_object(config.ProductionConfig)
    else:
        raise ValueError('Check FLASK_ENV')

    # ref. https://github.com/flask-restful/flask-restful/issues/280
    handle_exception = app.handle_exception
    handle_user_exception = app.handle_user_exception

    from .resources.foo import (
        foo_bp,
        Hello,
    )

    api_foo = Api(foo_bp)
    api_foo.add_resource(Hello, '/')

    app.register_blueprint(foo_bp)

    # ref. https://github.com/flask-restful/flask-restful/issues/280
    app.handle_exception = handle_exception
    app.handle_user_exception = handle_user_exception

    return app
