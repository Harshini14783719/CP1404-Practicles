from guitar import Guitar

FILENAME = "guitars.csv"


def main():

    guitars = load_guitars(FILENAME)
    print("These are my guitars: ")
    display_guitars(guitars)
    guitars.sort()
    print("\nSorted guitars: ")
    display_guitars(guitars)


def load_guitars(filename):
    """Read guitar data from file into list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a numbered list of guitars."""
    for i, guitar in enumerate(guitars):
        vintage = " (Vintage)" if guitar.is_vintage() else ""
        print(guitar, vintage)

main()