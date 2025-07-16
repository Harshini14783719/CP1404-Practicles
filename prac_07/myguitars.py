from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars(FILENAME)
    print("These are my guitars: ")
    display_guitars(guitars)
    guitars.sort()
    print("\nSorted guitars: ")
    display_guitars(guitars)
    print("\nadd new guitar to list:")
    add_new_guitars(guitars)
    save_guitars(FILENAME, guitars)


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


def add_new_guitars(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_add = Guitar(name, year, cost)
        guitars.append(guitar_add)
        print(f"{guitar_add} added.")
        name = input("Name: ")


def save_guitars(filename, guitars):
    """write all guitar data to the csv file"""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
