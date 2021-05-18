#!/usr/bin/python3
"""
    request api reddit and  parses the title of all hot
    articles, and prints a sorted count of given keywords
"""
import requests


def recursion(subreddit, dict_word, after):
    """ Request recursively and update the dict and finally print"""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=1000&after={}'\
          .format(subreddit, after)
    headers = {'user-agent': 'my-app/0.0.1'}
    result = requests.get(url, headers=headers)
    if result.status_code == 404 or len(result.json()) == 0:
        print('')
        return
    elif after == 'null' or after is None:
        keys = list(dict_word.keys())
        vals = list(dict_word.values())
        for v in sorted(dict_word.values(), reverse=True):
            if v > 0:
                print('{}: {:d}'.format(keys[vals.index(v)], v))
        return
    else:
        for element in result.json()['data']['children']:
            for key in dict_word:
                if key in element['data']['title']:
                    dict_word[key] += 1
        after = result.json()['data']['after']
        recursion(subreddit, dict_word, after)


def count_words(subreddit, word_list, after='t3_'):
    """transform the list into a dict and call the recursion function"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=1000&after={}'\
          .format(subreddit, after)
    dict_k = dict.fromkeys(word_list, 0)
    recursion(subreddit, dict_k, after)
