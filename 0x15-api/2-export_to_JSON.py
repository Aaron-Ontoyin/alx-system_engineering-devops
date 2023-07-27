#!/usr/bin/python3
"""
Uses REST AP and for a given employee ID,
returns info about his/her TODO list progress in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    empID = argv[1]
    URLID = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(empID)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(empID)

    employee = sessionReq.get(URLID)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    user = employeeName.json()['username']

    updatedUser = {}
    allTasks = []

    for emps in json_req:
        allTasks.append(
            {
                "task": emps.get('title'),
                "completed": emps.get('completed'),
                "username": user,
            })
    updatedUser[empID] = allTasks

    file_Json = empID + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updatedUser, f)
