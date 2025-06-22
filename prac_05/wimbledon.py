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
    records = read_wimbledon_data(FILENAME)
    champions_to_wins = count_champions(records)
    





def read_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        records = []
        for line in in_file:parts = line.strip().split(",")
            champion = parts[2]
            country = parts[1]
            records.append([champion, country])
        return records


def count_champions(records):
    champion_to_wins = {}
    for champion, _ in records:
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins