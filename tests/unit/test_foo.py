def test_hello_ok(tester):
    resp = tester.get(
        '/tests/hello',
        content_type='application/json',
    )

    assert {'Hello': 'World!'} == resp.get_json()
    assert 200 == resp.status_code


def test_secret_ok(tester, jwt):
    resp = tester.get(
        '/tests/secret',
        headers={'Authorization': 'Bearer {}'.format(jwt['access_token'])},
        content_type='application/json',
    )

    assert {'Hello': 'Secret!'} == resp.get_json()
    assert 200 == resp.status_code


def test_secret_without_header(tester):
    resp = tester.get(
        '/tests/secret',
        headers=None,
        content_type='application/json',
    )

    assert {'msg': 'Missing Authorization Header'} == resp.get_json()
    assert 401 == resp.status_code


def test_secret_with_refresh_token(tester, jwt):
    resp = tester.get(
        '/tests/secret',
        headers={'Authorization': 'Bearer {}'.format(jwt['refresh_token'])},
        content_type='application/json',
    )

    assert {'msg': 'Only access tokens are allowed'} == resp.get_json()
    assert 422 == resp.status_code


def test_secret_with_bad_access_token(tester, jwt):
    resp = tester.get(
        '/tests/secret',
        headers={'Authorization': 'Bearer {}extra-string'.format(jwt['access_token'])},
        content_type='application/json',
    )

    assert {'msg': 'Signature verification failed'} == resp.get_json()
    assert 422 == resp.status_code


def test_secret_with_bad_jwt(tester):
    resp = tester.get(
        '/tests/secret',
        headers={'Authorization': 'Bearer {}'.format('this-is-not-json-web-token')},
        content_type='application/json',
    )

    assert {'msg': 'Not enough segments'} == resp.get_json()
    assert 422 == resp.status_code


def test_secret_with_bad_header(tester):
    resp = tester.get(
        '/tests/secret',
        headers={'Authorization': '{}'.format('this-is-plain-text')},
        content_type='application/json',
    )

    assert {'msg': "Bad Authorization header. Expected value 'Bearer <JWT>'"} == resp.get_json()
    assert 422 == resp.status_code
