#!/usr/bin/python3
"""Number of subs to a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers to subreddit

    Parameters
    ----------
    subreddit: str
        The subreddit whose subsribers are to be found

    Returns
    -------
    Number of subscribers to a subreddit
    """
    url = f'https://oauth.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "Castro-Python"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    elif response.status_code == 302:
        return 0
    else:
        return 0
