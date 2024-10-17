#!/usr/bin/python3

import requests

# Function to fetch and print posts


def fetch_and_print_posts():
    # Send a GET request to the API
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Print the status code
    print(f"Status Code: {response.status_code}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()

        # Iterate over each post and print the title
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")
