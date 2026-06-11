import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_detail = response.json()
print(complete_detail[0]["user"]["login"])