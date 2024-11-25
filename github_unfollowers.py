import requests
import json


def get_followers(username, token, page):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url=f"https://api.github.com/users/{username}/followers?per_page=1000&page={page}", headers=headers)
    return response.json()


def get_following(username, token, page):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url=f"https://api.github.com/users/{username}/following?per_page=1000&page={page}", headers=headers)
    return response.json()


username = input("Enter your GitHub username: ")
token = input("Enter your token: ")

followers = []
unfollowers = []

page = 1
while get_followers(username, token, page):
    current_page = get_followers(username, token, page)

    for item in current_page:
        followers.append(item["login"])

    page += 1

page = 1
while get_following(username, token, page):
    current_page = get_following(username, token, page)

    for item in current_page:
        if item["login"] not in followers:
            unfollowers.append(item["login"])

    page += 1

for unfollower in unfollowers:
    print(f"https://github.com/{unfollower}")