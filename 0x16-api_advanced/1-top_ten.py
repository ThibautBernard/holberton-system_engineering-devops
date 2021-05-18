#!/usr/bin/python3
"""
    Request api reddit and return number of subscribers
    for a specific subreddit
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    result = requests.get(url, headers=headers)
    if result.status_code == 404:
        print(None)
    else:
        for element in result.json()['data']['children']:
            print(element['data']['title'])
