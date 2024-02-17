#!/usr/bin/python3
"""Queries Reddit Api
"""
import requests


def top_ten(subreddit):
    """Returns top 10 titles in a subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    agent = {'User-Agent': 'curl/1.0'}
    params = {'limit': 10}
    try:
        response = requests.get(url, headers=agent, params=params)
        response.raise_for_status()

        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children'][:10]:
                print(post['data']['title'])
    except requests.RequestException:
        print('None')


if __name__ == "__main__":
    import sys
    top_ten(sys.argv[1])
