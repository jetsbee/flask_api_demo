from flask import Blueprint
from flask_restful import Resource


foo_bp = Blueprint('foo', __name__)


class Hello(Resource):
    def get(self):
        return 'Hello, World!', 200
