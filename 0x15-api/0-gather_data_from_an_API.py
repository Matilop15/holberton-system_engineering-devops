#!/usr/bin/python3
"""
Given employee ID, returns information about his/her TODO list progress.
First line: Employee EMPLOYEE_NAME is done wit
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed
and non-completed tasks
"""

import requests
from sys import argv


if __name__ == '__main__':

    user = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    name = requests.get(user).json().get('name')
    req = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    request = requests.get(req)

    total = [task for task in request.json()]
    completed = [task for task in request.json() if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed), len(total)))
    for task in completed:
        print("\t {}".format(task.get('title')))
