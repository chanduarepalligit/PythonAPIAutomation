import requests
import json
from test_data import DataRead


def test_data():
    url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\Users\\Chandu\\Desktop\\StudentData.json", 'r')
    json_request = json.loads(file.read())
    obj = DataRead("C:\\Users\\Chandu\\Desktop\\TestData.xlsx", "Sheet1")
    cols = obj.column_count()
    rows = obj.row_count()
    keyList = obj.fetch_key_Names()
    for i in range(2, rows+1):
        json_data = obj.update_jsonRequest(i, json_request, keyList)
        response = requests.post(url, json_data)
        print(response.text)
