#!/usr/bin/python3
""" Gathers data from Employee API
"""
if __name__ == "__main__":
    import json
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
    json_file = id+'.json'
    my_dict = {id: []}
    with open(json_file, 'a') as f:
        for dic in todo_resp.json():
            new_dic = {
                    "task": dic["title"],
                    "completed": dic["completed"],
                    "username": name
                    }
            my_dict[id].append(new_dic)
        json.dump(my_dict, f)
