import requests
import json


class userApi:
    def __init__(self, url="https://petstore3.swagger.io/api/v3/user"):
        self.url = url
        self.headers = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def post_user(self, body):
        response = self.session.post(url =f"{self.url}", data = body, headers=self.headers)
        return response

    def post_user_list(self, body):
        response = self.session.post(url =f"{self.url}/createWithList", data = json.dumps(body), headers=self.headers)
        return response

    def get_user_login(self, username, password):
        response = self.session.get(url =f"{self.url}/login", params={"username": username, "password" : password}, headers=self.headers)
        return response

    def get_user_logout(self):
        response = self.session.get(url =f"{self.url}/logout", headers=self.headers)
        return response

    def get_user_by_user_name(self, username):
        response = self.session.get(url =f"{self.url}/{username}", headers=self.headers)
        return response

    def put_update_user(self, username):
        response = self.session.put(url =f"{self.url}/{username}", headers=self.headers)
        return response

    def delete_user(self, username):
        response = self.session.delete(url =f"{self.url}/{username}", headers=self.headers)
        return response
