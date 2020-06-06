import requests

url = "https://reqres.in/api/users/2"

resp = requests.delete(url)
print(resp.status_code)
