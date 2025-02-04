import json

import requests
from jsonschema import validate

url = "https://reqres.in/api/login"

payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

response = requests.request("POST", url, data=payload)

print(response.text)


def test_schema_validate_from_file():
    response = requests.post("https://reqres.in/api/users", data={"name": "morpheus", "job": "master"})
    body = response.json()

    assert response.status_code == 201
