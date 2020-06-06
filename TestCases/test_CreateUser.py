import requests
import jsonpath
import json
import pytest

url = "https://reqres.in/api/users"


@pytest.fixture()
def start_exec():
    global file
    file = open("C:\\Users\\Chandu\\Desktop\\PostData.json", 'r')

@pytest.mark.Smoke
def test_createNewUser(start_exec):
    json_input = file.read()
    json_read = json.loads(json_input)
    response = requests.post(url, json_read)
    assert response.status_code == 201


@pytest.mark.Sanity
def test_otherUser(start_exec):
    json_input = file.read()
    json_read = json.loads(json_input)
    response = requests.post(url, json_read)
    response_json = json.loads(response.text)
    get_id = jsonpath.jsonpath(response_json, 'id')
    print(get_id[0])
