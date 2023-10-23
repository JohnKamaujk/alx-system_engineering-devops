#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    else:
        return []


def get_tasks(user_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    )
    if response.status_code == 200:
        return response.json()
    else:
        return []


def main():
    all_users = get_users()
    all_employees_data = {}

    for user in all_users:
        user_id = user.get("id")
        tasks = get_tasks(user_id)

        user_data = [
            {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in tasks
        ]
        all_employees_data[str(user_id)] = user_data

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_data, json_file)


if __name__ == "__main__":
    main()
