import wikipedia


def main():
    print("Wikipedia Search Tool")
    while True:
        query = input("Enter page title: ").strip()
        if not query:
            print("Thank you.")

        try:
            # Attempt to fetch page details
            page = wikipedia.page(query, auto_suggest=False)
            print(f"\n{page.title}")
            print(wikipedia.summary(query, auto_suggest=False))
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10])  # Show first 10 options
        except wikipedia.exceptions.PageError:
            print('Page id "{}" does not match any pages. Try another id!'.format(query))


main()
