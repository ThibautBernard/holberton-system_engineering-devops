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
    list_tasks = []
    prev_user_id = 1
    req_user = "https://jsonplaceholder.typicode.com/users/1"
    info_user = requests.get(req_user).json()
    name_user = info_user['name']
    for content in response:
        """
            check if the user of the task has changed
            if has changed, request the name of the new user
            add into the dict new key (the user id) and all tasks
        """
        if content['userId'] != prev_user_id:
            req_user = "https://jsonplaceholder.typicode.com/users/{}"\
                      .format(content['userId'])
            info_user = requests.get(req_user).json()
            name_user = info_user['name']
            d[prev_user_id] = list_tasks
            list_tasks = []
        d_task = {}
        task = "{}".format(content['title'])
        complet = "{}".format(content['completed'])
        d_task['task'] = task
        d_task['completed'] = complet
        d_task['username'] = name_user
        list_tasks.append(d_task)
        prev_user_id = content['userId']
    with open('todo_all_employees.json', 'w', newline='') as file:
        json.dump(d, file)
