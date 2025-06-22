"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

print(CODE_TO_NAME)
final_entries = []
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        state_name = CODE_TO_NAME[state_code]
        final_entries.append((state_code, state_name))
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

print("\n Final Entries")
for code, name in final_entries:
    print(f"{code:3} is {name}")

