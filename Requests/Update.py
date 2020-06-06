import requests
import json
import jsonpath


url = "https://reqres.in/api/users/2"
file = open("C:\\Users\\Chandu\\Desktop\\PostData.json", 'r')
json_input = file.read()
request_json = json.loads(json_input)
response = requests.put(url, request_json)
response_json = json.loads(response.text)
job = jsonpath.jsonpath(response_json, 'Job')
print(response_json)
print(job[0])