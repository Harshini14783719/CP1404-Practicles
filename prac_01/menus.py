name = str(input("Enter name: "))
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>>").upper()
print("Finished.")
