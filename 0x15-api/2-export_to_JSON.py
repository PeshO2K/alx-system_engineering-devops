if __name__ == "__main__":
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_info = requests.get(base_url+"users/"+user_id).json()
    todos = requests.get(base_url+"todos",
                         params={"userId": user_id}).json()

    list_tasks = [{"task": todo.get('title'),
                   "completed": todo.get("completed"),
                   "username": user_info.get('username')} for todo in todos]
    json_name = f"{user_id}.json"
    with open(json_name, 'w') as jsonfile:
        json.dump({f'{user_info.get("id")}': list_tasks}, jsonfile)
