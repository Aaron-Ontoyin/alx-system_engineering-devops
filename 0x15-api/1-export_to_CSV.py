#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the CSV format.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    empID = argv[1]
    URLID = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(empID)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(empID)

    employee = sessionReq.get(URLID)
    employeeName = sessionReq.get(nameURL)

    jsonReq = employee.json()
    user = employeeName.json()['username']

    totalTasks = 0

    for done_tasks in jsonReq:
        if done_tasks['completed']:
            totalTasks += 1

    fileCSV = empID + '.csv'
    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in jsonReq:
            write.writerow([empID, user, i.get('completed'), i.get('title')])
