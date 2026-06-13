import requests

url = f"https://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get(url)

if response.status_code == 200:
    pull_requests = response.json()

    pr_creators = {}

    for pull in pull_requests:
        creator = pull["user"]["login"]
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1
        
    print("pr creator and theie counts")
    for creator, counts in pr_creators.items():
        print(f"{creator}: {counts} PR(s)")
else:
    print(f"data not found, status {response.status_code}")