#!/usr/bin/python3
""""
Script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys


def user_data_from_api(userId):
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
        )
    name = user.json().get('name')
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(userId)
        )
    data = response.json()

    total_task = len(data)
    completed_task = 0
    for task in data:
        if task.get('completed') is True:
            completed_task += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed_task, total_task))
    for task in data:
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    user_data_from_api(sys.argv[1])
