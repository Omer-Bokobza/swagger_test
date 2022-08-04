from store_petStore_swagger import storeApi
import pytest
import logging

log_format = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="log_file", format=log_format, filemode='w')
log = logging.getLogger()


@pytest.fixture()
def data():
    json = {
        "id": 4,
        "petId": 198772,
        "quantity": 7,
        "shipDate": "2022-08-03T02:44:28.669Z",
        "status": "approved",
        "complete": True
    }
    return json


def test_get_store_inventory():
    log.info("checking get store")
    check_get = storeApi().get_store_inventory()
    assert check_get.status_code == 200
    log.debug("test was successful")


def test_post_store_order(data):
    log.info("checking post store order")
    check_post = storeApi().post_store_order(body=data)
    assert check_post.status_code == 200
    assert check_post.json()["petId"] == data["petId"]
    log.debug("test was successful")


def test_get_order_id(data):
    log.info("checking get order id")
    assert data["id"] <= 5 or data["id"] > 10
    check_get = storeApi().get_order_id(orderId=data["id"])
    assert check_get.status_code == 200
    assert check_get.json()["id"] == data["id"]
    log.debug("test was successful")


def test_delete_pet(data):
    log.info("checking delete pet")
    assert data["id"] < 1000
    check_delete = storeApi().delete_pet(orderId=data["id"])
    assert check_delete.status_code == 200
    log.debug("test was successful")
