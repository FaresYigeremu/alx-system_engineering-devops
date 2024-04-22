import csv
import requests
import sys

def export_to_csv(employee_id):
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information using the provided employee ID
    user = requests.get(url + "users/{}".format(employee_id)).json()
    username = user.get("username")

    # Fetch the to-do list for the employee using the provided employee ID
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Prepare the CSV file name
    csv_file_name = "{}.csv".format(employee_id)

    # Write the data to the CSV file
    with open(csv_file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([employee_id, username, t.get("completed"), t.get("title")])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
