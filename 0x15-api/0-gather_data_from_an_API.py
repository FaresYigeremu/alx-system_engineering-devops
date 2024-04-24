#!/usr/bin/python3
"""fetch  to-do list info from employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for c in completed:
        print("\t {}".format(c))

