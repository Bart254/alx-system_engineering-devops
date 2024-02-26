#!/usr/bin/python3
"""Queries Reddit Api
"""
import requests


def top_ten(subreddit):
    """Returns top 10 titles in a subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    agent = {'User-Agent': 'Castro-Python'}
    try:
        response = requests.get(url, headers=agent,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
