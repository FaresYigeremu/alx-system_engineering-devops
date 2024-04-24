#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def fetch_employee_todos(employee_id):
    """Fetches and prints the to-do list information for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{base_url}users/{employee_id}").json()
    todos_response = requests.get(f"{base_url}todos", params={"userId": employee_id}).json()

    completed_todos = [todo.get("title") for todo in todos_response if todo.get("completed")]
    print(f"Employee {user_response.get('name')} is done with tasks({len(completed_todos)}/{len(todos_response)}):")
    for todo in completed_todos:
        print(f"\t{todo}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todos(employee_id)
