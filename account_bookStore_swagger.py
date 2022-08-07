import requests
import json


class accountApi:
    def __init__(self, url="https://bookstore.toolsqa.com/Account/v1"):
        self.url = url
        self.headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def post_account_auth(self, body):
        response = self.session.post(url=f"{self.url}/Authorized", json=body , headers=self.headers)
        return response

    def post_generate_token(self, body):
        response = self.session.post(url=f"{self.url}/GenerateToken", json=body, headers=self.headers)
        return response

    def post_User(self, body):
        response = self.session.post(url=f"{self.url}/User", json = body ,  headers=self.headers)
        return response

    def delete_User(self, UUID, auth):
        response = self.session.delete(url=f"{self.url}/User/{UUID}", headers=auth)
        return response

    def get_user(self, UUID, auth):
        response = self.session.get(url=f"{self.url}/User/{UUID}", headers=auth)
        return response
