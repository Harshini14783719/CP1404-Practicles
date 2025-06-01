
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90
score = float(input("Enter score: "))
if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
    result = "Invalid score"
elif score >= EXCELLENT_SCORE:
    result = "Excellent"
elif score >= PASSABLE_SCORE:
    result = "Passable"
else:
    result = "bad"

print(result)