from pet_petStore_swagger import petApi
import pytest
import logging

log_format = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="log_file", format=log_format, filemode='w')
log = logging.getLogger()


@pytest.fixture()
def data():
    json = {
        "id": 10,
        "name": "doggie",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    return json


def test_put_Pet(data):
    log.info("checking put pet")
    check_put = petApi().put_Pet(body=data)
    assert check_put.status_code == 200
    assert check_put.json()["id"] == data["id"]
    log.info("update name")
    data["name"] = "lucky"
    check_put = petApi().put_Pet(body=data)
    assert check_put.status_code == 200
    assert check_put.json()["name"] == "lucky"
    log.debug("test was successful")


def test_post_Pet(data):
    log.info("checking post pet")
    check_post = petApi().post_Pet(body=data)
    assert check_post.status_code == 200
    assert check_post.json()["id"] == data["id"]
    log.debug("test was successful")


def test_find_by_status():
    log.info("checking find pet by status")
    status = ["available", "pending", "sold"]
    for s in status:
        checkget = petApi().find_by_status(status=s)
        d = checkget.json()
        assert checkget.status_code == 200
        for pet in d:
            assert pet["status"] == s
    log.debug("test was successful")


def test_find_by_tags():
    log.info("checking find pet by tags")
    tags = ["string"]
    check_get = petApi().find_by_tags(tags=tags)
    d = check_get.json()
    assert check_get.status_code == 200
    for pet in d:
        # find the pet tags in petApi
        assert len([x for x in pet["tags"] if (x["name"] in tags)]) > 0
    log.debug("test was successful")


def test_pet_id(data):
    log.info("checking pet id")
    checkget = petApi().pet_id(id=data["id"])
    assert checkget.status_code == 200
    assert checkget.json()["id"] == data["id"]
    log.debug("test was successful")


def test_post_pet_id(data):
    log.info("checking post pet id")
    checkpost = petApi().post_pet_id(id=data["id"], name="david", status="sold")
    assert checkpost.status_code == 200
    d = checkpost.json()
    assert d["id"] == data["id"]
    assert d["name"] == "david"
    assert d["status"] == "sold"
    log.debug("test was successful, pet was added")


def test_delete_pet(data):
    log.info("checking delete pet")
    check_delete = petApi().delete_pet(api_key="omer", id=data["id"])
    assert check_delete.status_code == 200
    assert check_delete.text == 'Pet deleted'
    log.debug("test was successful, pet deleted")
