"""
estimated time: 2 hours
time taken:
"""

from project import Project
from datetime import datetime

FILENAME = "projects.txt"

MENU = """\nMenu:
L - Load projects  
S - Save projects  
D - Display projects  
F - Filter projects by date  
A - Add new project  
U - Update project  
Q - Quit"""


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}.")
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename to save to: ")
            save_projects(filename,projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects()


def load_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, start_date, priority, cost_estimate,completion_percentage = line.strip().split(',')
            projects.append(Project(name, datetime.strptime(start_date, "%d/%m/%Y").date(), int(priority), float(cost_estimate), int(cost_estimate)))
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as out_file:
        for project in projects:
            print(f"{project.name}, {project.start_date}, {project.priority}, {project.cost_estimate}, {project.completion_percentage}", file=out_file)


def display_projects(projects):
    for i, project in enumerate(projects):
        print(project)


def filter_projects(projects):
    date_string = input("Enter date to show projects after that date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    filtered_projects.sort()
    for project in filtered_projects:
        print(project)


def add_new_projects(projects):
    name = input("Name: ")
    while name != "":
        start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        priority = int(input("Enter Priority rate: "))
        cost_estimate = float(input("Enter cost estimate: "))
        completion_percentage = int(input("Enter Completion percentage: "))
        project_add = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project_add)
        print(f"{project_add} Added")
        name = input("Name:")

    