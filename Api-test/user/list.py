import requests
from getpass import getpass

password =getpass()
get_token = requests.post("http://localhost:8000/api/auth/", json={"username": "lopez", "password": password})
token = (get_token.json().get("token"))

headers = {"Authorization": f"Token {token}"}
url = "http://localhost:8000/api/users/"
res = requests.get(url, headers=headers)
print(res.status_code)
print(res.json())