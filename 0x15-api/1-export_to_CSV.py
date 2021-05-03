#!/usr/bin/python3
"""
    request api and write in csv file
    all tasks todo for an user
"""
import csv
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
    name_user = info_user['name']
    with open('{}.csv'.format(info_user['id']), 'w') as file:
        for content in response:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            id_us = content['userId']
            complet = content['completed']
            content = content['title']
            writer.writerow([id_us, name_user, complet, content])
