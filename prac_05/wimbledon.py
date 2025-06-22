"""
wimbledon.py

Write a program to read this file, process the data and display processed information:
the champions and how many times they have won.
the countries of the champions in alphabetical order

Estimated time: 30 minutes
Actual time:
"""

FILENAME = "wimbledon.csv"

def main():



def read_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        records = []
        for line in in_file:parts = line.strip().split(",")
            champion = parts[2]
            country = parts[1]
            records.append([champion, country])
        return records