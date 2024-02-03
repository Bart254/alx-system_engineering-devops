#!/usr/bin/python3
""" Gathers data from Employee API
"""
if __name__ == "__main__":
    import json
    import requests

    user_data = {}
    todo_resp = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_resp = requests.get("https://jsonplaceholder.typicode.com/users/")
    json_file = "todo_all_employees.json"

    for user in user_resp.json():
        user_id = user["id"]
        username = user["username"]
        key = str(user_id)
        value = []
        for todo in todo_resp.json():
            if todo["userId"] == user_id:
                my_dict = {"username": username,
                           "task": todo["title"],
                           "completed": todo["completed"]
                           }
                value.append(my_dict)
        user_data[key] = value

    with open(json_file, 'w') as file:
        json.dump(user_data, file)
