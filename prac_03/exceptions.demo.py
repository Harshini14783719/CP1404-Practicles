"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
 when the inputted value is not an integer
2. When will a ZeroDivisionError occur?
# when 0 is the entered denominator value
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

