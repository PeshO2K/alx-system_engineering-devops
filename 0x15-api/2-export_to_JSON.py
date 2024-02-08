#!/usr/bin/python3
'''script to get data from rest api'''
import csv
import json
import requests
import sys


def gather_data(emp_id):
    '''get data of employee id'''

    api_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

    response = requests.get(api_url)
    tasks = requests.get(todo_url)
    try:
        edata = response.json()
        tdata = tasks.json()
        return(edata, tdata)
    except Exception:
        print(Exception)


def completed_tasks(data_tuple):
    edata = data_tuple[0]
    tdata = data_tuple[1]
    emp_name = edata['name']
    tcompleted = [task for task in tdata if task['completed'] is True]
    # print(tcompleted)
    tdone = len(tcompleted)
    ttotal = len(tdata)
    ttitles = "\n\t " + \
        "\n\t ".join([task['title'] for task in tcompleted])

    my_comp_tasks = "".join(
        [f"Employee {emp_name} is done with tasks({tdone}/{ttotal}):",
            ttitles])
    print(my_comp_tasks)


def to_csv(data_tuple):
    '''create csv file'''
    edata = data_tuple[0]
    tdata = data_tuple[1]
    alltasks = [{"USER_ID": edata['id'], "USERNAME": edata['username'],
                "TASK_COMPLETED_STATUS": task['completed'],
                 "TASK_TITLE": task['title']} for task in tdata]
    filename = f"{edata['id']}.csv"

    # Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    # print(alltasks)
    with open(filename, 'w', newline='') as csvfile:
        fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fields,
                                quoting=csv.QUOTE_ALL)
        for task in alltasks:
            writer.writerow(task)


def to_json(data_tuple):
    '''export to json'''
    edata = data_tuple[0]
    tdata = data_tuple[1]
    user_id = edata['id']
    alltasks = [{"task": task['title'],
                "completed": task['completed'],
                 "username": edata['username']} for task in tdata]

    json_data = {user_id: alltasks}

    filename = f"{user_id}.json"

    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():

        to_json(gather_data(int(sys.argv[1])))
    else:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
