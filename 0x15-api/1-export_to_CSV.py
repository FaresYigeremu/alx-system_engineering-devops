#!/usr/bin/python3
'''Python script that conver data into csv'''
import csv
import requests
import sys


def export_to_csv(employee_id):

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(employee_id)).json()
    username = user.get("username")

    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    csv_file_name = "{}.csv".format(employee_id)

    with open(csv_file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow(
                [employee_id, username, t.get("completed"), t.get("title")])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
