from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_add = Guitar(name, year, cost)
        guitars.append(guitar_add)

