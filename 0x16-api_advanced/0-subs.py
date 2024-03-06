#!/usr/bin/python3
"""Returns the number of subs to a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my-app/0.0.1' + 'CastroPy' + 'Caz'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        return 0

    data = response.json()
    return data['data']['subscribers']
