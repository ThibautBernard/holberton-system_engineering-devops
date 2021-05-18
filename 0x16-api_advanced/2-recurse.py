#!/usr/bin/python3
"""
    request api reddit and return a list of all
    hot article recursively
"""
import requests


def recurse(subreddit, hot_list=[], after='t3_'):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=1000&after={}'\
         .format(subreddit, after)
    headers = {'user-agent': 'my-app/0.0.1'}
    result = requests.get(url, headers=headers)
    if result.status_code == 404 or len(result.json()) == 0:
        return None
    elif after == 'null' or after is None:
        return
    else:
        for element in result.json()['data']['children']:
            hot_list.append(element['data']['title'])
        after = result.json()['data']['after']
        recurse(subreddit, hot_list, after)
        return hot_list
