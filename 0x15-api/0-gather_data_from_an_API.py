#!/usr/bin/python3
""" Gathers data from Employee API
"""
if __name__ == "__main__":
    import requests
    import sys

    id = sys.argv[1]
    todo_values = {'userId': id}
    todo_resp = requests.get('https://jsonplaceholder.typicode.com/todos/',
                             params=todo_values)
    user_values = {'id': id}
    user_resp = requests.get('https://jsonplaceholder.typicode.com/users/',
                             params=user_values)
    name = user_resp.json()[0]['name']
    total = 0
    done = 0
    title = []
    for dictionary in todo_resp.json():
        if dictionary['completed']:
            done += 1
            title.append(dictionary['title'])
        total += 1
    print(f'Employee {name} is done with tasks({done}/{total}):')
    for task in title:
        print(f'\t {task}')
