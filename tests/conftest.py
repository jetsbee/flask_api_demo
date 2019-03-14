import pytest
import json

from flask_pymongo import PyMongo

from flask_api_demo import create_app


app = create_app()

if app.config['ENV'] != 'testing':
    raise ValueError('Check FLASK_ENV')


@pytest.fixture(scope='session')
def reset_testing_db():
    mongo = PyMongo(app)
    cx = mongo.cx

    yield reset_testing_db

    cx.drop_database('flask_api_demo_test')


@pytest.fixture(scope='session')
def tester(reset_testing_db):
    tester = app.test_client()

    return tester


@pytest.fixture(scope='session')
def jwt(tester):
    resp = tester.post(
        '/users/registration',
        data=json.dumps({'username': 'test', 'password': 'test'}),
        content_type='application/json',
    )
    resp_data = resp.get_json()
    result = {
        'access_token': resp_data['access_token'],
        'refresh_token': resp_data['refresh_token'],
    }

    return result
