#!/usr/bin/python3
"""
    request api and write in csv file
    all tasks todo for an user
"""
import csv
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
        name_user = info_user['name']
        with open('{}.csv'.format(sys.argv[1]), 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for content in response:
                id_us = content['userId']
                complet = content['completed']
                content = content['title']
                writer.writerow([id_us, name_user, complet, content])
