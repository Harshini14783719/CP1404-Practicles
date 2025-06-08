# 1)
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2)
in_file = open("name.txt", "r")
name_from_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_from_file}!")

# 3)
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    result = first_number + second_number
    print("The sum of the first two numbers is:", result)

# 4)
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print("The total of all numbers is:", total)