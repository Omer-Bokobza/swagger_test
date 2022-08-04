from user_petStore_swagger import userApi
import pytest
import logging

log_format = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="log_file", format=log_format, filemode='w')
log = logging.getLogger()


@pytest.fixture()
def data():
    json = {
        "id": 10,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 1
    }
    return json


def test_post_user(data):
    log.info("checking post user")
    check_post = userApi().post_user(body=data)
    assert check_post.status_code == 200
    assert check_post.json()["id"] == data["id"]
    log.debug("test was successful")


def test_post_user_list(data):
    log.info("checking post list of users")
    check_post = userApi().post_user_list(body=data)
    assert check_post.status_code == 200
    assert check_post.json()["id"] == data["id"]
    log.debug("test was successful")


def test_get_user_login(data):
    log.info("checking get user login")
    check_get = userApi().get_user_login(username=data["username"], password=data["password"])
    assert check_get.status_code == 200
    log.debug("test was successful")


def test_get_user_logout():
    log.info("checking get user logout")
    check_get = userApi().get_user_logout()
    assert check_get.status_code == 200
    log.debug("test was successful")


def test_get_user_by_user_name(data):
    log.info("checking get user by username")
    check_get = userApi().get_user_by_user_name(username=data["username"])
    assert check_get.status_code == 200
    assert check_get.json()["username"] == data["username"]
    log.debug("test was successful")


def test_put_update_user(data):
    log.info("checking put update user")
    check_put = userApi().put_update_user(username=data["username"])
    assert check_put.status_code == 200
    assert check_put.json()["username"] == data["username"]
    log.info("update name")
    data["username"] = "omer bokobza"
    check_put = userApi().put_update_user(username=data["username"])
    assert check_put.status_code == 200
    assert check_put.json()["username"] == data["username"]
    log.debug("test was successful")


def test_delete_user(data):
    log.info("checking delete pet")
    check_delete = userApi().delete_user(username=data["username"])
    assert check_delete.status_code == 200
    log.debug("test was successful, user deleted")
