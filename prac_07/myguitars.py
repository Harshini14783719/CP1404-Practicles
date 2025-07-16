from guitar import Guitar

FILENAME = "guitars.csv"


def main():

    guitars = load_guitars(FILENAME)


def load_guitars(filename):
    """Read guitar data from file into list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars