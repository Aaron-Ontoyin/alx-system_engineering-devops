#!/usr/bin/python3
"""
Uses REST API and for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    reqSession = requests.Session()

    empID = argv[1]
    URLID = "https://jsonplaceholder.typicode.com/users/{}/todos".format(empID)
    nameURL = "https://jsonplaceholder.typicode.com/users/{}".format(empID)

    employee = reqSession.get(URLID)
    employeeName = reqSession.get(nameURL)

    jsonReq = employee.json()
    name = employeeName.json().get("name")

    totalTasks = 0
    for doneTasks in jsonReq:
        if doneTasks["completed"]:
            totalTasks += 1

    print(
        "Employee {} is done with tasks({}/{}):".format(
            name, totalTasks, len(jsonReq)
        )
    )

    for doneTasks in jsonReq:
        if doneTasks["completed"]:
            print("\t " + doneTasks.get("title"))
