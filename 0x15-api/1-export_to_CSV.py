#!/usr/bin/python3
""" Gathers data from Employee API
Then exports it into csv file
"""
if __name__ == "__main__":
    import requests
    import sys
    import csv

    user_id = int(sys.argv[1])
    name = ""
    user_data = []
    todo_resp = requests.get("https://jsonplaceholder.typicode.com/todos/")
    user_resp = requests.get("https://jsonplaceholder.typicode.com/users/")

    for a_dict in user_resp.json():
        if a_dict["id"] == user_id:
            name = a_dict["name"]
            break

    for todo in todo_resp.json():
        if todo["userId"] == user_id:
            my_dict = {"id": user_id, "name": name,
                       "status": todo["completed"], "title": todo["title"]
                       }
            user_data.append(my_dict)
    csv_file = str(user_id) + '.csv'
    fields = ["id", "name", "status", "title"]
    with open(csv_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fields, quoting=csv.QUOTE_ALL)
        writer.writerows(user_data)
