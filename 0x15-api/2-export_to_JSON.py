#!/usr/bin/python3
"""
    request api and write in JSON file
    all tasks todo for an user
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        req = "https://jsonplaceholder.typicode.com/users/{}/todos"\
              .format(sys.argv[1])
        response = requests.get(req).json()
        req_use = "https://jsonplaceholder.typicode.com/users/{}"\
                  .format(sys.argv[1])
        info_user = requests.get(req_use).json()
        name_user = info_user['username']
        d = {}
        list_tasks = []
        for content in response:
            d_task = {}
            d_task['task'] = content['title']
            d_task['completed'] = content['completed']
            d_task['username'] = name_user
            list_tasks.append(d_task)
        d[sys.argv[1]] = list_tasks
        with open('{}.json'.format(sys.argv[1]), 'w') as f:
            json.dump(d, f)
