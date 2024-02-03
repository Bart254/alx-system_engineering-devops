#!/usr/bin/python3
""" Gathers data from Employee API
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    user_id = int(sys.argv[1])
    username = ""
    user_data = {}
    key = str(user_id)
    value = []
    todo_resp = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_resp = requests.get("https://jsonplaceholder.typicode.com/users/")

    for a_dict in user_resp.json():
        if a_dict["id"] == user_id:
            username = a_dict["username"]
            break

    for todo in todo_resp.json():
        if todo["userId"] == user_id:
            my_dict = {"task": todo["title"],
                       "completed": todo["completed"],
                       "username": username
                       }
            value.append(my_dict)
            user_data[key] = value
    json_file = str(user_id) + '.json'
    with open(json_file, 'w') as file:
        json.dump(user_data, file)
