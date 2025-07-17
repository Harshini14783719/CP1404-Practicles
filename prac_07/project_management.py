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
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects(FILENAME)
        elif choice == "S":
            




def load_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, start_date, priority, cost_estimate,completion_percentage = line.strip().split(',')
            projects.append(Project(name, datetime.strptime(start_date, "%d/%m/%Y").date(), int(priority), float(cost_estimate), int(cost_estimate)))
    return projects