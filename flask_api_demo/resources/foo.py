from flask import Blueprint
from flask_restful import Resource
from flask_jwt_extended import jwt_required


foo_bp = Blueprint('foo', __name__, url_prefix='/tests')


class Hello(Resource):
    def get(self):
        return {'Hello': 'World!'}, 200


class HelloSecret(Resource):
    @jwt_required
    def get(self):
        return {'Hello': 'Secret!'}, 200

