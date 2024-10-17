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

import csv

# Function to fetch posts and save them to a CSV file
def fetch_and_save_posts():
    # Send a GET request to the API
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()

        # Prepare a list of dictionaries containing only id, title, and body
        formatted_posts = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

        # Write the data to a CSV file
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])

            # Write the header
            writer.writeheader()

            # Write the posts
            writer.writerows(formatted_posts)

        print("Data successfully saved to posts.csv.")
    else:
        print("Failed to fetch posts.")

