"""
estimated time: 2 hours
time taken:
"""

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
        if choice == "L"



def load_projects(filename):
