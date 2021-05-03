#!/usr/bin/python3
"""
    request api
"""
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
    name_user = requests.get(req_use).json()['name']
    tmp = "Employee {} is done with tasks({:d}/{:d}):"
    print(tmp.format(name_user, len(task_completed), total_tasks))
    for content in response:
        if content['completed']:
            print("\t{}".format(content['title']))
