from account_bookStore_swagger import accountApi
import pytest
import logging

log_format = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="log_file", format=log_format, filemode='w')
log = logging.getLogger()

@pytest.fixture()
def data():
    json = {
        "userName": "omer1",
        "password": "Aa123456@"
    }
    return json

@pytest.fixture()
def data_user():
    userid = "3a1e70f5-87f6-4cc3-a209-015532cc7b7a"
    return userid

@pytest.fixture()
def data_token():
    token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6Inlvc2kiLCJwYXNzd29yZCI6IkFhMTIzNDU2QCIsImlhdCI6MTY1OTgwNjAwMX0.xoxNcb_a_KX-QpSf6MAVCIpiN1LOLE12fboaIlra-To"
    return token


def test_post_user(data):
    check_post = accountApi().post_User(body=data)
    assert check_post.status_code == 201
    assert data["userName"] == check_post.json()["username"]

def test_generate_token(data):
    check_post = accountApi().post_generate_token(body=data)
    assert check_post.status_code == 200
    assert check_post.json()["status"] == 'Success'

def test_post_account_auth(data):
    check_post = accountApi().post_account_auth(body=data)
    assert check_post.status_code == 200
    assert check_post.text == 'true'

def test_get_user(data_user,data):
    token = accountApi().post_generate_token(body=data)
    assert token.status_code == 200
    assert token.json()["status"] == 'Success'
    check_get = accountApi().get_user(UUID=data_user, auth={'Authorization': 'Bearer ' + token.json()['token']})
    assert check_get.status_code == 200
    assert check_get.json()['userId'] == data_user

def test_delete_User(data_user, data):
    token = accountApi().post_generate_token(body=data)
    assert token.status_code == 200
    assert token.json()["status"] == 'Success'
    check_get = accountApi().delete_User(UUID=data_user, auth={'Authorization': 'Bearer ' + token.json()['token']})
    assert check_get.status_code == 200
