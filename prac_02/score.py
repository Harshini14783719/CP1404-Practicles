import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90


def main():
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(result)

    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(f"Random score: {random_score: .2f}")
    print(f"Result for random score: {determine_score(random_score)}")


def determine_score(score):
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        result = "Invalid score"
    elif score >= EXCELLENT_SCORE:
        result = "Excellent"
    elif score >= PASSABLE_SCORE:
        result = "Passable"
    else:
        result = "bad"
    return result


main()
