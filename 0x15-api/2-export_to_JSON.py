#!/usr/bin/python3
"""
    request api and write in JSON file
    all tasks todo for an user
"""
import json
import requests
import sys


if __name__ == "__main__":
    req = "https://jsonplaceholder.typicode.com/users/{}/todos"\
           .format(sys.argv[1])
    response = requests.get(req).json()
    total_tasks = len(response)
    task_completed = [i for i, k in enumerate(response) if k['completed']]
    req_use = "https://jsonplaceholder.typicode.com/users/{}"\
              .format(sys.argv[1])
    info_user = requests.get(req_use).json()
    name_user = info_user['username']
    d = {}
    list_tasks = []
    for content in response:
        d_task = {}
        task = "{}".format(content['title'])
        complet = "{}".format(content['completed'])
        d_task['task'] = task
        d_task['completed'] = complet
        d_task['username'] = name_user
        list_tasks.append(d_task)
    d[info_user['id']] = list_tasks
    with open('{}.json'.format(info_user['id']), 'w', newline='') as file:
        json.dump(d, file)
