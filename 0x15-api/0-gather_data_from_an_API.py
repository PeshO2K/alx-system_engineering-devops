#!/usr/bin/python3
'''script to get data from rest api'''
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
        # print(tcompleted)
        tdone = len(tcompleted)
        ttotal = len(tdata)
        ttitles = "\n\t ".join([task['title'] for task in tcompleted])

        # print(tdata)
    else:
        tasks.raise_for_status()
    print(f"Employee {emp_name} is done with tasks({tdone}/{ttotal}):")
    print("\t", ttitles)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        gather_data(int(sys.argv[1]))
    else:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
