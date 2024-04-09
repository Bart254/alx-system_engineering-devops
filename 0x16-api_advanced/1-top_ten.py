#!/usr/bin/python3
"""Top ten hot posts
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts

    Paramters
    ---------
    subreddit: str
        The subreddit whose top ten posts are to be printed
    """
    headers = {'User-Agent': 'Castro-Python'}
    r = requests.get('https://oauth.reddit.com/r/{}/hot.json?limit=10'.format(
        subreddit), headers=headers, allow_redirects=False)
    if r.status_code < 300:
        json = r.json()
        data_dict = json.get('data')
        hot_list = data_dict.get('children')
        for post in hot_list:
            sub_data_dict = post.get('data')
            print(sub_data_dict.get('title'))
    else:
        print(None)
