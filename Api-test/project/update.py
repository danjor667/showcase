import requests
from getpass import getpass

username = input("enter username: ")
password = getpass()
pk = input("what is the pk of the project you want to update: ")
pk = int(pk)


url = f"http://localhost:8000/api/projects/{pk}/update/"

res = requests.delete(url)
print(res.json())