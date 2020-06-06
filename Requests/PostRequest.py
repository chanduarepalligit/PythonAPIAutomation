import requests
import json
import jsonpath

url = "https://reqres.in/api/users"
file = open("C:\\Users\\Chandu\\Desktop\\PostData.json", 'r')
json_input = file.read()
json_read = json.loads(json_input)
response = requests.post(url, json_read)
print(response.content)
response_json = json.loads(response.text)
get_id = jsonpath.jsonpath(response_json, 'id')
print(get_id[0])
