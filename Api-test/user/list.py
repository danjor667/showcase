import requests
from getpass import getpass
password = "Jordan1995"

#headers = {"Authorization": f"Token {token}"}
url = "http://localhost:8000/api/auth/"
res = requests.post(url, json={"username": "jordan", "password": password})
print(res.status_code)
token = (res.json())

#### trying creating a user