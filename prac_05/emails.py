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


def extract_name_from_email(email):
    name_part = email.split('@')
    parts = name_part.replace('.', ' ').replace('_', ' ')
    return ' '.join(parts)