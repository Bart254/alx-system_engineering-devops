#!/usr/bin/python3
"""Returns the number of subs to a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers)

    # Check if the response status code indicates success
    if response.status_code == 200:
        data = response.json()

        # Check if the response contains the expected data
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    elif response.status_code == 302:
        # Redirect to search results, indicating an invalid subreddit
        return 0
    else:
        return 0
