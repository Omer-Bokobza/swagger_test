from bookStore_bookStore_swagger import BookStoretApi
from account_bookStore_swagger import accountApi
import pytest
import logging

# add your specific path to filename to get the log text file
log_format = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="log_file", format=log_format, filemode='w')
log = logging.getLogger()

@pytest.fixture()
def auth():
    json = {
        "userName": "omerB38",
        "password": "Aa123456@"
    }
    return json

@pytest.fixture()
def post_data():
    data = {
        "userId": "f738dea3-73b6-4768-a250-cc4911bc5a10",
        "collectionOfIsbns": [
            {
                "isbn": "15616"
            }
        ]
    }
    return data


@pytest.fixture()
def data():
    json = {
        "isbn": "9781449325862",
        "title": "string",
        "subTitle": "string",
        "author": "string",
        "publish_date": "2022-08-07T00:43:07.596Z",
        "publisher": "string",
        "pages": 0,
        "description": "string",
        "website": "string"
    }
    return json

@pytest.fixture()
def userId():
    return "f738dea3-73b6-4768-a250-cc4911bc5a10"

def pytest_configure():
    pytest.token = ""
    pytest.ISBN = ""


def test_post_Books(auth, data):
    authorized = accountApi().post_generate_token(body = auth)
    assert authorized.status_code == 200
    assert authorized.json()["status"] == 'Success'
    pytest.token = authorized.json()['token']
    check_post = BookStoretApi().post_Books(body=data, headers={'Authorization': 'Bearer ' + pytest.token})
    assert check_post.status_code == 200

def test_get_Books(data):
    check_get = BookStoretApi().get_Books()
    assert check_get.status_code == 200


def test_put_Books(data):
    check_put = BookStoretApi().put_Books(body=data, ISBN="9781449325862")
    assert check_put.status_code == 200


def test_delete_Books(userId):
    check_delete = BookStoretApi().delete_Books(UserId=userId)
    assert check_delete.status_code == 200


def test_get_Book():
    check_get = BookStoretApi().get_Book(ISBN="9781449325862")
    assert check_get.status_code == 200


def test_delete_Book(data):
    check_delete = BookStoretApi().delete_Book(body=data)
    assert check_delete.status_code == 200
