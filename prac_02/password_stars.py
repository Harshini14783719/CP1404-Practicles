MINIMUM_LENGTH = 2


def main():
    password = get_valid_password()
    print_asterisks(password)


def get_valid_password():
    password = str(input("Enter password: "))
    while len(password) < MINIMUM_LENGTH:
        print("Invalid Password")
        password = str(input("Enter password: "))
    return password