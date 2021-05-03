#!/usr/bin/python3
"""
    request api and write in JSON file
    all tasks todo for every users
"""
import json
import requests
import sys


if __name__ == "__main__":
    req = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(req).json()
    d = {}
    req_user = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(req_user).json()
    for user in users:
        reso_todos = "https://jsonplaceholder.typicode.com/users/{}/todos"\
              .format(user['id'])
        rq = requests.get(reso_todos).json()
        list_tasks = []
        for content in rq:
            d_task = {}
            task = "{}".format(content['title'])
            complet = "{}".format(content['completed'])
            d_task['task'] = task
            d_task['completed'] = complet
            d_task['username'] = user['username']
            list_tasks.append(d_task)
        d[user['id']] = list_tasks
    with open('todo_all_employees.json', 'w') as f:
        json.dump(d, f)
