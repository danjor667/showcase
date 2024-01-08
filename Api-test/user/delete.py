import requests
from getpass import getpass

password = getpass()
get_token = requests.post("http://localhost:8000/api/auth/", json={"username": "jordan", "password": password})
token = (get_token.json().get("token"))
pk = input("enter pk: ")
pk = int(pk)
headers = {"Authorization": f"Token {token}"}
url = f"http://localhost:8000/api/users/{pk}/delete/"
res = requests.delete(url, headers=headers)
print(res.status_code)
