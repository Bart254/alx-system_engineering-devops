#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    "Gets top ten hots"
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data['data']['children']

    for i in range(10):
        if i < len(posts):
            print(posts[i]['data']['title'])
        else:
            break
