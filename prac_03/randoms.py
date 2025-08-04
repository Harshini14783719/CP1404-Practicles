import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# Line 1: 18

# What was the smallest number you could have seen, what was the largest?
# smallest: 5
# Largest: 20

# What did you see on line 2?
# Line 2: 9

# What was the smallest number you could have seen, what was the largest?
# smallest: 3
# Largest: 9

# Could line 2 have produced a 4?
# no, line 2 could not a produces a 4.

# What did you see on line 3?
# 3.3472611688886453

# What was the smallest number you could have seen, what was the largest?
# Smallest: 2.5
# Largest: 5.5

random_number = random.randint(1,100)
print(f"A random number between 1 to 100 is: {random_number}")
