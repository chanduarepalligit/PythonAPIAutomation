import requests
import jsonpath
import json


def test_oauth():
    Token_URL = "http://thetestingworldapi.com/Token"
    data = {'grant_type': 'password', 'username': 'admin', 'password': 'admin'}
    response = requests.post(Token_URL, data)
    token = jsonpath.jsonpath(response.json(), 'access_token')
    auth = {'Authorization': 'Bearer ' + token[0]}
    Api_URL = "http://thetestingworldapi.com/api/StDetails/1104"
    response = requests.get(Api_URL, headers=auth)
    print(response.text)
    print(response.status_code)
