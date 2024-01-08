import requests
from getpass import getpass

username = input("enter username: " )
password = getpass()
gettoken = f'http://localhost:8000/api/auth/'
token_res = requests.post(gettoken, json={"username":username, "password":password})
if token_res.status_code ==200:
    print(token_res.status_code)
    pk = int(input("enter the project id: "))
    token = token_res.json().get("token")
    headers = {"Authorization": f"Token {token}"}
    url = f"http://localhost:8000/api/projects/{pk}/delete/"
    res = requests.delete(url, headers=headers)
    print(res.status_code)
