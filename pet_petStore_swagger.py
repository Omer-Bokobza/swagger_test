import requests
import json


class petApi:
    def __init__(self, url="https://petstore3.swagger.io/api/v3/pet"):
        self.url = url
        self.headers = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def put_Pet(self, body):
        response = self.session.put(url =f"{self.url}", data = body, headers=self.headers)
        return response

    def post_Pet(self, body):
        response = self.session.post(url =f"{self.url}", data = body, headers=self.headers)
        return response

    def find_by_status(self, status):
        response = self.session.get(url =f"{self.url}/findByStatus", params={"status": status}, headers=self.headers)
        return response

    def find_by_tags(self, tags):
        response = self.session.get(url =f"{self.url}/findByTags", params={"tags": tags}, headers=self.headers)
        return response

    def pet_id(self, id):
        response = self.session.get(url =f"{self.url}/{id}", headers=self.headers)
        return response

    def post_pet_id(self, id, name, status):
        response = self.session.post(url=f"{self.url}/{id}", params = {"name" : name, "status": status}, headers=self.headers)
        return response

    def delete_pet(self, api_key, id):
        del_header = {"api_key" : api_key}
        response = self.session.delete(url=f"{self.url}/{id}", headers= del_header)
        return response

    #def upload_photo(self, photo)
