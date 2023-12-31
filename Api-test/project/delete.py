import requests
from getpass import getpass

username = input("enter username: " )
password = getpass()
pk = input("what is the pk of the project you want to delete: ")
pk = int(pk)
gettoken = f'http://localhost:8000/api/auth/'
token_res = requests.post(gettoken, json={"username":username, "password":password})
if token_res.status_code ==200:
    token = token_res.json().get("token")
    headers = {"Authorization": f"Token {token}"}
    url = f"http://localhost:8000/api/projects/{pk}/delete/"
    res = requests.delete(url, headers=headers)
    print(res.status_code)
