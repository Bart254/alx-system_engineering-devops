#!/usr/bin/python3
"""Returns a list of all hot articles for a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursive function that returns the list of all
    hot articles in a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Curl'}
    if after:
        params = {'after': after}
    else:
        params = {}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            new_after = data['data']['after']
            if new_after:
                return recurse(subreddit, hot_list, new_after)
            else:
                return hot_list
        return hot_list
    except requests.RequestException:
        return None


if __name__ == "__main__":
    import sys
    result = recurse(sys.argv[1])
    if result:
        print(len(result))
