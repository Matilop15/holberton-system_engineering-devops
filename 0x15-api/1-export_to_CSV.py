#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
"""

if __name__ == '__main__':

    import requests
    from sys import argv
    import csv

    f_name = argv[1] + ".csv"
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1]))
    name = user.json()
    req = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                       .format(argv[1]))
    todos = req.json()

    with open(f_name, 'w', newline='') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            w.writerow([name['id'], name['username'],
                        todo['completed'], todo['title']])
