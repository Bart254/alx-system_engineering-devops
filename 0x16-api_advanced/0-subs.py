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
    url = f'https://oauth.reddit.com/r/{subreddit}/about'
    headers = {"User-Agent": "Castro-Python", "Authorization": "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzEyNzYxMzg4LjY5OTY1NywiaWF0IjoxNzEyNjc0OTg4LjY5OTY1NywianRpIjoiU1lnUVluWVd6UXllMmlGRl94WEM2N3ZKRzJTbC13IiwiY2lkIjoiekRZeVJpQmlEeUpLRmJhVjZOMUdpZyIsImxpZCI6InQyX3h5YXExMzhydSIsImFpZCI6InQyX3h5YXExMzhydSIsImxjYSI6MTcxMjY3MTc0NzQ2MSwic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iOjl9.jke9Ls5juh5zEwYct3b-mjnsljrbue0lQcQP7QxTSHBMLXDuiAipJzNWSToz99yK4-2yclVrjqcoeyYRinm3BhAahZ6V0WphCxTGjst7hpdkZ8ZMkzW8Liq7UHRVDGzJbDSSWKxy-58NZ-YIDXkV8cQkVek0nqV25xDtzvmYGiIAku9bcBal0edCB2ooLEQyvmpJRHPZb4Zdj5iOrx0KtYWn1Hqyu0OAxeD0M_c2FOyAMqs8gXVS2oOLNALdM8FJ5-8yTSJNSgkeRiFgvXwQfM3RIpdg6ib4yIfPDqtaTwsNfn_Z2-yij_bYeOTMMvFFxzjG2sARhQ9d9JkZACmvfg"}

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
