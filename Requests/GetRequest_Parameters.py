import requests

params = {"id": 2}
response = requests.get("https://reqres.in/api/users", params=params)
print(response.text)


name = 'chandu'
pars = {"name": name, "email": 'chandu.a@gmail.com'}
response = requests.get("https://httpbin.org/get", params=pars)
print(response.text)
