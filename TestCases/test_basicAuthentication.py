import requests
from requests.auth import HTTPBasicAuth


def test_auth():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth("chanduarepalligit","Fightclub@1992"))
    print(response.text)
