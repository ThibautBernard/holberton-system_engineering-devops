#!/usr/bin/python3
"""
    Request api reddit and return number of subscribers
    for a specific subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    result = requests.get(url, headers=headers)
    if result.status_code == 404:
        return 0
    return result.json()['data']['subscribers']
