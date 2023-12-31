import requests
url = "http://localhost:8000/api/projects/create/"

res = requests.post(url, json={}, data={})
print(res.json())