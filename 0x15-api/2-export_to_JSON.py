#!/usr/bin/python3
""" contains a python script that, using the JSONplaceholder API, for a given
    employee ID, returns information about employees todo list progress """
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()
    # todo variable = grabs all todos (completed or not) for the user passed in
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(userId)).json()
    taskslist = []
    for task in todo:
        mydict = {}
        mydict["task"] = task.get('title')
        mydict["completed"] = task.get('completed')
        mydict["username"] = name.get('username')
        taskslist.append(mydict)
    jsonobj = {}
    jsonobj[userId] = taskslist
    with open("{}.json".format(userId), 'w') as ajsonfile:
        json.dump(jsonobj, ajsonfile)
