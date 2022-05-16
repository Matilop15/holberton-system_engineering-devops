#!/usr/bin/python3
"""
Using what you did in the task #0, 
extend your Python script to export data in the JSON format.
"""

if __name__ == '__main__':

    import requests
    from sys import argv
    import json

    f_name = argv[1] + ".json"
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1]))
    name = user.json()
    req = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                       .format(argv[1]))
    todos = req.json()

    with open(f_name, 'w', newline='') as f:
        tasks = [dict(task=todo['title'], completed=todo['completed'],
                 username=name['username']) for todo in todos]
        d = {}
        d[argv[1]] = tasks
        f.write(json.dumps(d, f))
