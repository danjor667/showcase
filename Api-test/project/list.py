import requests
from getpass import getpass

url = "http://localhost:8000/api/projects/"

ans = requests.get(url)
print(ans.json())