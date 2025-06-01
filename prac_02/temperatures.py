MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            get_fahrenheit()
            return get_fahrenheit()
        elif choice == "F":
            get_celsius()
            return get_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_fahrenheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit: .2f} F")


def get_celsius():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius: .2f} °C")


main()