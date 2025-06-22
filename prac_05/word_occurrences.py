def main():
    text = input("Text: ").strip()
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0)+1

    sorted_words = sorted(word_count.keys())

    for word in sorted_words:
        print(f"{word}: {word_count[word]}")


main()