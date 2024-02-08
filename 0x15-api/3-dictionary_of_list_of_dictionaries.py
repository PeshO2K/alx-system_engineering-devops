#!/usr/bin/python3
'''script to get data from rest api'''
import json
import requests


def gather_data():
    '''get data of employee id'''

    api_url = f"https://jsonplaceholder.typicode.com/users/"
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}"

    response = requests.get(api_url)
    # tasks = requests.get(todo_url)
    all_employees_data = {}

    try:
        edata = response.json()
        for employee in edata:
            emp_id = employee['id']
            emp_url = todo_url.format(emp_id)
            tasks = requests.get(emp_url)
            tdata = tasks.json()
            alltasks = [{"username": employee['username'],
                         "task": task['title'],
                         "completed": task['completed']} for task in tdata]

            all_employees_data[emp_id] = alltasks

        # Write all data to a single JSON file
        with open('todo_all_employees.json', 'w') as jsonfile:
            json.dump(all_employees_data, jsonfile)

        # tdata = tasks.json()
        # return(edata)  #, tdata)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # if len(sys.argv) == 2 and sys.argv[1].isdigit():
    gather_data()
