MINIMUM_LENGTH = 2


def main():
    password = get_name()
    print_asterisks(password)


def get_name():
    password = str(input("Enter password: "))
    while len(password) < MINIMUM_LENGTH:
        print("Invalid Password")
        password = str(input("Enter password: "))
    return password


def print_asterisks(password):
    print("*" * len(password))


main()