import requests
import json
from DataDriven import Library


def test_add_multiple_students():
    APi_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\Users\\Chandu\\Desktop\\StudentData.json")
    json_request = json.loads(file.read())
    obj = Library.DataRead("C:\\Users\\Chandu\\Desktop\\TestData.xlsx", "Sheet1")
    cols = obj.column_count()
    rows = obj.row_count()
    keyList = obj.fetch_KeyNames()

    for i in range(2, rows+1):
        updated_json_request = obj.update_request_with_data(i, json_request, keyList)
        response = requests.post(APi_URL, updated_json_request)
        print(response.text)
