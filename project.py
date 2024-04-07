import sys
import calendar
from datetime import date
from tabulate import tabulate
import csv
import re

class Create:
        def __init__(self, task, udate):
            self.task = task
            self.udate = udate

        def get_task(self):
            return self._task

        def get_date(self):
            return self.udate

        @property
        def task(self):
            return self._task

        @task.setter
        def task(self, task):
            if not task :
                raise ValueError("Missing task")
            self._task = task

        @property
        def udate(self):
            return self._udate

        @udate.setter
        def udate(self, udate):
            t = date.today()
            if date.fromisoformat(udate) and get_date(udate) > t:
                self._udate = udate
            else:
                raise ValueError("Invalid Date")

def main():
    tasks = []
    if sys.argv[1].lower() == "add":
        tasks = []
        numoftasks = int(input("How many tasks do you want to add? "))
        for _ in range(numoftasks):
            task = Create(input("Task: "), input("When do you want to do this task? "))
            tasks.append({"Date": task.get_date(), "Tasks": task.get_task()})
        with open("tasks.txt", "a") as taskfile:
            writer = csv.DictWriter(taskfile, fieldnames = ["Date", "Tasks"])
            writer.writerow({"Date": "Date", "Tasks": "Tasks"})
            add_to_file(tasks, taskfile)

    elif sys.argv[1].lower() == "view":
        datev = input("Month and year: ").strip().capitalize()
        if matches := re.search(r"^[a-z]+, [0-9]{4}$", datev, re.IGNORECASE):
            monthyear = datev.split(", ")
        else:
            sys.exit("Date format should be (month_name, YYYY)")
        tasklist = get_from_file(monthyear)
        print(tabulate(tasklist, tablefmt = "rounded_grid", headers = {"Date": "Date", "Tasks": "Tasks"} ))
        
    elif sys.argv[1].lower() == "remove":
        etasks = []
        rdate = input("Which date's task do you want to remove? ")
        if date.fromisoformat(rdate):
            with open("tasks.txt", "r") as filer:
                reader = csv.DictReader(filer)
                for line in reader:
                    if line["Date"] != rdate:
                        etasks.append({"Date": line["Date"], "Tasks": line["Tasks"]})
            if etasks == []:
                sys.exit("No task in this date")
            with open("tasks.txt", "w") as filex:
                writer = csv.DictWriter(filex, fieldnames = ["Date", "Tasks"])
                writer.writerow({"Date": "Date", "Tasks": "Tasks"})
                add_to_file(etasks, filex)
                print("removed")
                                               

    elif sys.argv[1].lower() == "help":
        print("""
Add: To add task
View: To view task
Remove: To remove task
              """)

def add_to_file(tasks, filename):
        writer = csv.DictWriter(filename, fieldnames = ["Date", "Tasks"])
        for task_info in tasks:
            writer.writerow({"Date": task_info["Date"], "Tasks": task_info["Tasks"]})

def get_from_file(monthyear):
    c = calendar.Calendar(0)
    to_return = []
    monthnum = get_month_num(monthyear[0])
    year = int(monthyear[1])
    t = date.today()
    with open("tasks.txt") as taskfile:
        reader = csv.DictReader(taskfile)
        for line in reader:
            for a in c.itermonthdays(year, monthnum):
                if a != 0:
                    dater = date(year, monthnum, a)
                    if dater.year >= t.year and dater.month >= t.month:
                        datef = line["Date"].split("-")
                        if dater.year == int(datef[0]) and dater.month == int(datef[1]) and dater.day == int(datef[2]):
                            to_return.append({"Date": f"{get_month_name(monthnum)} {a}, {year}", "Tasks": line["Tasks"]})
                    else:
                        sys.exit("Cannot access past tasks")
    if to_return == []:
        sys.exit("No tasks in this month")
    return to_return


def get_date(udate):
    datex = udate.split("-")
    return date(int(datex[0]), int(datex[1]), int(datex[2]))

def get_month_num(name):
    months = ["January", "February", "March", "April",
               "May", "June", "July", "August",
               "September", "October", "November", "December"]
    if name in months:
        return months.index(name) + 1
    raise ValueError("Invalid month")

def get_month_name(n):
    months = ["January", "February", "March", "April",
               "May", "June", "July", "August",
               "September", "October", "November", "December"]
    return months[n - 1]

if __name__ == "__main__":
    main()
