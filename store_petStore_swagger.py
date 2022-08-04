import requests
import json


class storeApi:
    def __init__(self, url="https://petstore3.swagger.io/api/v3/store"):
        self.url = url
        self.headers = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def get_store_inventory(self):
        response = self.session.get(url=f"{self.url}/inventory", headers=self.headers)
        return response

    def post_store_order(self, body):
        response = self.session.post(url=f"{self.url}/order", data=body, headers=self.headers)
        return response

    def get_order_id(self, orderId):
        response = self.session.get(url=f"{self.url}/order/{orderId}", params={"orderId": orderId},
                                    headers=self.headers)
        return response

    def delete_pet(self, orderId):
        response = self.session.delete(url=f"{self.url}/order/{orderId}", params={"orderId": orderId},
                                       headers=self.headers)
        return response
