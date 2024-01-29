#!/usr/bin/python3
""" Gathers data from Employee API
"""
if __name__ == "__main__":
    import json
    import requests

    users = []
    user_resp = requests.get('https://jsonplaceholder.typicode.com/users')
    for dic in user_resp.json():
        user_dict = {'id': dic["id"], 'username': dic["username"]}
        users.append(user_dict)
    json_file = 'todo_all_employees.json'
    my_dict = {}
    with open(json_file, 'a') as f:
        for user in users:
            id = user['id']
            my_dict[id] = []
            todo_values = {'userId': id}
            todo_req = 'https://jsonplaceholder.typicode.com/todos/'
            todo_resp = requests.get(todo_req, params=todo_values)
            for dic in todo_resp.json():
                new_dic = {
                            "username": user['username'],
                            "task": dic["title"],
                            "completed": dic["completed"],
                            }
                my_dict[id].append(new_dic)
        json.dump(my_dict, f)
