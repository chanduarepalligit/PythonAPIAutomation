import requests
import jsonpath
import json


def test_add_details():
    global get_id
    Api_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\Users\\Chandu\\Desktop\\StudentData.json", 'r')
    json_request = json.loads(file.read())
    response = requests.post(Api_URL, json_request)
    get_id = jsonpath.jsonpath(response.json(), 'id')
    print(get_id[0])


def test_get_details():
    Api_URL = "http://thetestingworldapi.com/api/studentsDetails/"+str(get_id[0])
    response = requests.get(Api_URL)
    print(response.text)

