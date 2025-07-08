import requests
from prettytable import PrettyTable

print("GITHUB USER ACTIVITY")

username = input("Enter Username: ")

api_url = f"https://api.github.com/users/{username}/events"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    for item in data:
        item_type = item["type"]
        item_name = item["repo"]["name"]

        if item_type == "PushEvent":
            commit_count = len(item["payload"]["commits"])
            print(f"- pushed {commit_count} at {item_name}")
                
        if item_type == "IssuesEvent":
            action = item["payload"]["action"]

            if action == "opened":
                issue_title = item["payload"]["issue"]["title"]
                print(f"- pushed {issue_title} at {item_name}")

        if item_type == "WatchEvent":
            action = item["payload"]["action"]

            if action == "started": 
                print(f"- Starred {item_name}")