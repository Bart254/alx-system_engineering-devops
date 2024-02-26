#!/usr/bin/python3
"""Queries Reddit Api
"""
import requests


def top_ten(subreddit):
    """Returns top 10 titles in a subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    agent = {'User-Agent': 'Castro-Python'}
    params = {'limit': 10}
    response = requests.get(url, headers=agent, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print('None')
    else:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
