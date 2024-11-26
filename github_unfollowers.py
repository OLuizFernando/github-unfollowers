import requests
import json


def safe_get(url, headers):
    """
    Makes a safe GET request and handles potential errors.
    """
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []


def fetch_users(endpoint, username, token):
    """
    Fetches a list of users (followers or following) from the GitHub API.
    """
    headers = {"Authorization": f"token {token}"}
    users = set()
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/{endpoint}?per_page=100&page={page}"
        current_page = safe_get(url, headers)
        if not current_page:  # Stop if no more data is returned
            break
        users.update(item["login"] for item in current_page)
        page += 1
    return users


def main():
    username = input("Enter your GitHub username: ")
    token = input("Enter your GitHub Personal Access Token: ")

    print("Fetching followers and following data... This may take a while.")

    # Fetch followers and following
    followers = fetch_users("followers", username, token)
    following = fetch_users("following", username, token)

    # Find users who don't follow back
    unfollowers = following - followers

    # Output the result
    if unfollowers:
        print("\nUsers who don't follow you back:\n")
        for user in unfollowers:
            print(f"https://github.com/{user}")
    else:
        print("Everyone you follow follows you back!")

    print("\nProcess completed!")


if __name__ == "__main__":
    main()
