"""
estimated time: 2 hours
time taken:
"""

from project import Project
from datetime import datetime

FILENAME = "projects.txt"

MENU = """ - (L)oad projects   
 - (S)ave projects  
 - (D)isplay projects  
 - (F)ilter projects by date  
 - (A)dd new project  
 - (U)pdate project  
 - (Q)uit"""


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
            filter_projects(projects)
        elif choice == "A":
            add_new_projects(projects)
        elif choice == "U":
            update_project(projects)

        print(MENU)
        choice = input(">>> ").upper()

    save = input("Would you like to save to projects.txt? ").title()
    if save == "Yes":
        save_projects(FILENAME, projects)
        print("Projects saved.")

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        next(in_file)
        for line in in_file:
            name, start_date, priority, cost_estimate,completion_percentage = line.strip().split('\t')
            projects.append(Project(name,
                                    start_date,
                                    int(priority),
                                    float(cost_estimate),
                                    int(completion_percentage)))
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as out_file:
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display incomplete and completed projects separately, sorted by priority."""
    incomplete = [project for project in projects if not project.is_complete()]
    completed = [project for project in projects if project.is_complete()]

    # Sort both groups by priority (lower number = higher priority)
    incomplete.sort()
    completed.sort()

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
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
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    start_date = start_date_string
    priority = int(input("priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project_add = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project_add)
    save_projects(FILENAME, projects)


def update_project(projects):
    """Update a project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        project_to_update = projects[choice]
    except (ValueError, IndexError):
        print("Invalid project number.")
        return

    print(project_to_update)

    new_completion = input("New Percentage: ").strip()
    if new_completion:
        try:
            project_to_update.completion_percentage = int(new_completion)
        except ValueError:
            print("Invalid percentage. Update skipped.")

    new_priority = input("New Priority: ").strip()
    if new_priority:
        try:
            project_to_update.priority = int(new_priority)
        except ValueError:
            print("Invalid priority. Update skipped.")


main()
