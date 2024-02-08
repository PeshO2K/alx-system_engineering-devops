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
        ttitles = "\n\t " + "\n\t ".join([task['title'] for task in tcompleted])

        my_comp_tasks = "".join(
            [f"Employee {emp_name} is done with tasks({tdone}/{ttotal}):",
                ttitles])
        print(my_comp_tasks)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():

        completed_tasks(gather_data(int(sys.argv[1])))
    else:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
