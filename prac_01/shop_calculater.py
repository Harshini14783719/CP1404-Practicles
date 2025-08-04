DISCOUNT_PRICE_LIMIT = 100
DISCOUNT_VALUE = 0.9
NUMBER_OF_ITEMS_LIMIT = 0
number_of_items = int(input("Enter the number of items bought: "))
while number_of_items < NUMBER_OF_ITEMS_LIMIT:
    print("Invalid number of items!")
    number_of_items = int(input("Enter the number of items bought: "))
total_price = 0
for i in range(number_of_items):
    price = float(input(f"Enter the price of items: "))
    total_price += price

if total_price > DISCOUNT_PRICE_LIMIT:
    total_price *= DISCOUNT_VALUE
print(f"Total price for {number_of_items} is ${total_price: .2f}")
