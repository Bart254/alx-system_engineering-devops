#!/usr/bin/python3
"""Queries Reddit Api
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the no of subs in a subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    agent = {'User-Agent': 'Castro-Python'}
    response = requests.get(url, headers=agent, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data.get('data').get('subscribers')
