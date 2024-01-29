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
    name = user_resp.json()[0]['username']
    csv_file = id+'.csv'
    with open(csv_file, 'a') as f:
        for dic in todo_resp.json():
            string = '"{}","{}","{}","{}"\n'.format(id, name, dic["completed"],
                                                    dic["title"])
            f.write(string)
