import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users?page=2"


@pytest.mark.Smoke
def test_fetchUserDetails():
    response = requests.get(url)
    json_response = json.loads(response.text)
    # print(json.dumps(json_response, indent=4))
    pages = jsonpath.jsonpath(json_response, 'total_pages')
    print(pages[0])
    for i in range(0, 3):
        first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
        print(first_name[0])
