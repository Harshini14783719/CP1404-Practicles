"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
SALES_VALUE = 1000
LOW_SALE_BONUS_VALUE = 0.10
HIGH_SALE_BONUS_VALUE = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < SALES_VALUE:
        bonus = sales * LOW_SALE_BONUS_VALUE
        print(f"You get a bonus of {bonus}")
    elif sales >= SALES_VALUE:
        bonus = sales * HIGH_SALE_BONUS_VALUE
        print(f"You get a bonus of: {bonus}")
    sales = float(input("Enter sales: $"))
print("invalid number")
