#!/usr/bin/python3
'''script to get data from rest api'''
import csv
import requests
import sys


def gather_data(emp_id):
    '''get data of employee id'''

    api_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

    response = requests.get(api_url)
    tasks = requests.get(todo_url)
    if (response.ok):
        edata = response.json()
        emp_name = edata['name']
        # print(edata)
    else:
        response.raise_for_status()
    if (tasks.ok):
        tdata = tasks.json()
        tcompleted = [task for task in tdata if task['completed'] is True]
        alltasks = [{"USER_ID": emp_id, "USERNAME": emp_name,
                     "TASK_COMPLETED_STATUS": task['completed'], "TASK_TITLE": task['title']} for task in tcompleted]
        # print(tcompleted)
        tdone = len(tcompleted)
        ttotal = len(tdata)
        ttitles = "\n\t ".join([task['title'] for task in tcompleted])

        # print(tdata)
    else:
        tasks.raise_for_status()
    my_output = "\t".join([f"Employee {emp_name} is done with tasks({tdone}/{ttotal}):",
                          ttitles])
    # print(my_output)
    filename = f"{emp_id}.csv"

    # Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    # print(alltasks)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for task in alltasks:
            writer.writerow(task)
    # return(my_output)


    # cdata = [emp_id, emp_id, task['completed'], task['title'] for task in tdata]
    # print(cdata)
    # with open(filename, w)



if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        gather_data(int(sys.argv[1]))
    else:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
