import requests
import json
import jsonpath


def test_add_studentData():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\Users\\Chandu\\Desktop\\StudentData.json", 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL, json_request)
    print(response.text)


# def test_update_studentData():
#     API_URL = "http://thetestingworldapi.com/api/studentsDetails/237697"
#     file = open("C:\\Users\\Chandu\\Desktop\\StudentData.json", 'r')
#     json_request = json.loads(file.read())
#     response = requests.put(API_URL, json_request)
#     print(response.text)


def test_delete_studentData():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/269044"
    response = requests.delete(API_URL)
    print(response.text)


def test_get_studentData():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/237697"
    response = requests.get(API_URL)
    print(response.text)
    json_response = response.json()
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 237697