#!/usr/bin/python3
"""Queries Reddit Api
"""
import requests


def top_ten(subreddit):
    """Returns top 10 titles in a subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    agent = {'User-Agent': 'curl/1.0'}
    try:
        response = requests.get(url, headers=agent)
        response.raise_for_status()

        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children'][:10]:
                print(post['data']['title'])
    except requests.RequestException:
        print('None')
