import requests

url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

response = requests.get(url)
#print(response.status_code)

if response.status_code == 200:
    pull_requests = response.json()
    #print(pull_requests)

    pr_creators = {}
    
    for pull in pull_requests:
        creator = pull["user"]["login"]
        #print(creator)
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1
        #print(pr_creators)

    print("PR creators and Counts:")
    #print(pr_creators.items())
    for creator, count in pr_creators.items():
        print(f"{creator}: {count}' PR(s)")
else:
    print(f"Failed to fetch Data. Status code {response.status_code}")


