NAME_TO_COLOR_CODE = {
    "ALICE BLUE": "#f0f8ff",
    "AMETHYST": "#9966cc",
    "ANTIQUEWHITE3": "#cdc0b0",
    "AQUA": "#00ffff",
    "BAKER MILLER PINK": "#ff91af",
    "CADETBLUE1": "#98f5ff",
    "DARK LAVENDER": "#734f96",
    "FLORALWHITE": "#fffaf0",
    "GOLDEN POPPY": "#fcc200",
    "ICEBERG": "#71a6d2"
}

print(NAME_TO_COLOR_CODE)

color_name = input("Enter color name: ").upper()
while color_name != "":
    try:
        print(f"{color_name} is {NAME_TO_COLOR_CODE[color_name]}")
    except KeyError:
        print("Invalid color")
    color_name = input("Enter color name: ").upper()
