"""
emails.py

A program that stores users' emails (unique keys) and names (values) in a dictionary.

Estimate time: 25 minutes
Actual time: 20 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        default_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {default_name}? (y/n)").strip().lower()
        if confirmation == "" or confirmation == "y":
            name = default_name
        else:
            name = input("Name: ").strip()

        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    name_part = email.split('@')
    parts = name_part.replace('.', ' ').replace('_', ' ')
    return ' '.join(parts)


main()