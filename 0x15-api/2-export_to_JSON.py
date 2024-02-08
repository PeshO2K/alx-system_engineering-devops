#!/usr/bin/python3
"""a Python script that exports to JSON"""
import json
import requests


if __name__ == "__main__":
    """a function that exports JSON dictionary of list of dictionaries"""
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    dictionary = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = requests.get("{}/{}/todos".format(url, user_id)).json()
        dict_list = []
        for task in tasks:
            if (task.get("userId") == user_id and task.get("completed")):
                tmp_dict = {}
                tmp_dict["task"] = task.get("title")
                tmp_dict["completed"] = task.get("completed")
                tmp_dict["username"] = username
                dict_list.append(tmp_dict)
        dictionary[user_id] = dict_list

    with open("todo_all_employees.json", "w+") as file:
        json.dump(dictionary, file)
