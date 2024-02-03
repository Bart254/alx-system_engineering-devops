#!/usr/bin/python3
""" Gathers data from Employee API
"""
if __name__ == "__main__":
    import requests
    import sys

    user_id = int(sys.argv[1])
    name, total, complete = ["", 0, 0]
    completed_todos = []
    todo_resp = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_resp = requests.get("https://jsonplaceholder.typicode.com/users/")

    for a_dict in user_resp.json():
        if a_dict["id"] == user_id:
            name = a_dict["name"]
            break

    for todo in todo_resp.json():
        if todo["userId"] == user_id:
            total += 1
            if todo["completed"]:
                complete += 1
                completed_todos.append(todo["title"])

    print(f'Employee {name} is done with tasks({complete}/{total}):')
    for title in completed_todos:
        print(f'\t {title}')
