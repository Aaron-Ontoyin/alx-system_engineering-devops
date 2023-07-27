#!/usr/bin/python3
"""
Uses REST API and for a given employee ID,
returns info about his/her TODO list progress in the JSON format.
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    allTodos = {}
    for user in users:
        tasks = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                taskDict = {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                }
                tasks.append(taskDict)
        allTodos[user.get("id")] = tasks

    with open("todo_all_employees.json", mode="w") as f:
        json.dump(allTodos, f)
