import wikipedia


def main():
    print("Wikipedia Search Tool")
    while True:
        query = input("Enter page title: ").strip()
        if not query:
            print("Thank you.")

        