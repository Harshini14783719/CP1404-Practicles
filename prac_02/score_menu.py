MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90


def main():

    score = get_valid_score()

    while True:
        print("\nMenu:\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Farewell!")
            break
        else:
            print("Invalid choice.")


def get_valid_score():

    score = float(input("Enter score (0-100): "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score


def determine_result(score):

    if score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):

    print("*" * int(round(score)))


main()