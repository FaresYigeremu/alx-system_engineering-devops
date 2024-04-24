#!/usr/bin/python3
"""Fetch to-do list info from employee ID."""
import requests
import sys


def fetch_employee_info(user_id):
    """Fetch employee information from the API."""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    return response.json()


def fetch_todos(user_id):
    """Fetch to-do list for the given employee ID."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})
    return response.json()


def get_completed_tasks(todos):
    """Filter and return completed tasks."""
    return [todo.get("title") for todo in todos if todo.get("completed")]


def print_todo_info(user, todos):
    """Print employee's name and completed tasks."""
    completed_tasks = get_completed_tasks(todos)
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t{}".format(task))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    user = fetch_employee_info(user_id)
    todos = fetch_todos(user_id)
    print_todo_info(user, todos)
