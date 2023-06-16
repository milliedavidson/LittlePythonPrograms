# Replace "YOUR_ACCESS_TOKEN" with your actual Mastodon access token, which you can 
# get by registering an application on your Mastodon instance

# https://docs.joinmastodon.org/client/intro/

import requests
import json

def mastodon_bot(base_url, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Get user information
    user_response = requests.get(f"{base_url}/api/v1/accounts/verify_credentials", headers=headers)
    user_data = user_response.json()
    user_id = user_data["id"]

    # Create a toot (post)
    toot_data = {
        "status": "Hello, Mastodon!"
    }
    toot_response = requests.post(f"{base_url}/api/v1/statuses", headers=headers, data=json.dumps(toot_data))
    if toot_response.status_code == 200:
        print("Toot created successfully.")
    else:
        print("Error creating toot.")

    # Like a toot
    toot_id = input("Enter the ID of the toot you want to like: ")
    like_response = requests.post(f"{base_url}/api/v1/statuses/{toot_id}/favourite", headers=headers)
    if like_response.status_code == 200:
        print("Toot liked successfully.")
    else:
        print("Error liking toot.")

    # Follow a user
    user_to_follow_id = input("Enter the ID of the user you want to follow: ")
    follow_response = requests.post(f"{base_url}/api/v1/accounts/{user_to_follow_id}/follow", headers=headers)
    if follow_response.status_code == 200:
        print("User followed successfully.")
    else:
        print("Error following user.")

    # Unfollow a user
    user_to_unfollow_id = input("Enter the ID of the user you want to unfollow: ")
    unfollow_response = requests.post(f"{base_url}/api/v1/accounts/{user_to_unfollow_id}/unfollow", headers=headers)
    if unfollow_response.status_code == 200:
        print("User unfollowed successfully.")
    else:
        print("Error unfollowing user.")

    # Retrieve user timeline
    timeline_response = requests.get(f"{base_url}/api/v1/accounts/{user_id}/statuses", headers=headers)
    timeline_data = timeline_response.json()
    if timeline_response.status_code == 200:
        for toot in timeline_data:
            print(f"Toot ID: {toot['id']}, Content: {toot['content']}")
    else:
        print("Error retrieving user timeline.")

# Base URL of the Mastodon instance
base_url = input("Enter the base URL of the Mastodon instance (see: https://mastodonservers.net/servers): ")

# Access token for authentication
access_token = input("Enter your Mastodon access token: ")

# Call the Mastodon bot function
mastodon_bot(base_url, access_token)

