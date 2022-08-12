import requests
import json


class BookStoretApi:
    def __init__(self, url="https://bookstore.toolsqa.com/swagger/Account/v1"):
        self.url = url
        self.headers = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def get_Books(self):
        response = self.session.get(url =f"{self.url}/Books", headers=self.headers)
        return response

    def post_Books(self, body, headers):
        response = self.session.post(url =f"{self.url}/Books", json = body, headers=headers)
        return response

    def delete_Books(self, UserId):
        response = self.session.delete(url =f"{self.url}/Books", params={"UserId": UserId}, headers=self.headers)
        return response

    def get_Book(self, ISBN):
        response = self.session.get(url =f"{self.url}/Book", params={"ISBN": ISBN}, headers=self.headers)
        return response

    def delete_Book(self, body):
        response = self.session.delete(url =f"{self.url}/Book", json = body, headers=self.headers)
        return response

    #replaceIsbn means replace path?
    def put_Books(self, body, ISBN):

        response = self.session.put(url =f"{self.url}/Books/{ISBN}", json = body, headers=self.headers)
        return response
