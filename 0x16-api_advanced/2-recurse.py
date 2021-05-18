#!/usr/bin/python3
"""
    request api reddit and return a list of all
    hot article recursively
"""
import requests


def recurse(subreddit, hot_list=[], counter=0, after='t3_'):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=1&after={}'\
         .format(subreddit, after)
    headers = {'user-agent': 'my-app/0.0.1'}
    result = requests.get(url, headers=headers)
    if result.status_code == 404 or len(result.json()) == 0:
        return None
    else:
        hot_list.append(result.json()['data']['children'][0]['data']['title'])
        counter += 1
        after = result.json()['data']['after']
        recurse(subreddit, hot_list, counter, after)
        return hot_list
