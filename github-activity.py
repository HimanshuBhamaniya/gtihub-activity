import requests
import argparse

def fetch_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {"User-Agent": "github-activity-cli"}  # GitHub requires a User-Agent
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error fetching data:", response.status_code)
        return

    events = response.json()
    for event in events[:10]:
        print(f"- {event['type']} at {event['created_at']} in {event['repo']['name']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitHub User Activity CLI")
    parser.add_argument("username", help="GitHub username")
    args = parser.parse_args()

    fetch_activity(args.username)