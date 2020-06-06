import requests

headers = {'name': 'chandu', 'job': 'testing'}
response = requests.get("https://httpbin.org/get", headers=headers)
print(response.content)
