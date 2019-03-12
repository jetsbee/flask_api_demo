from flask import Flask
from flask_restful import Api

from .resources.foo import foo_bp
from .resources.foo import Hello


def create_app():
    app = Flask(__name__)
    api_foo = Api(foo_bp)

    # ref. https://github.com/flask-restful/flask-restful/issues/280
    handle_exception = app.handle_exception
    handle_user_exception = app.handle_user_exception

    api_foo.add_resource(Hello, '/')
    app.register_blueprint(foo_bp)

    # ref. https://github.com/flask-restful/flask-restful/issues/280
    app.handle_exception = handle_exception
    app.handle_user_exception = handle_user_exception

    return app
