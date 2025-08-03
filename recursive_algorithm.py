
"""def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disc 1 from {source} to {target}")
    else:
        tower_of_hanoi(n - 1, source, auxiliary, target)
        print(f"Move disc {n} from {source} to {target}")
        tower_of_hanoi(n - 1, auxiliary, target, source)


# Ask for user input
num_discs = int(input("Enter the number of discs: "))

# Calculate total number of moves
total_moves = 2 ** num_discs - 1

# Output steps and total move count
print(f"\nSteps to solve Tower of Hanoi with {num_discs} discs:\n")
tower_of_hanoi(num_discs, 'A', 'C', 'B')
print(f"\nTotal moves required: {total_moves}")"""

"""
CP1401 2025-2 Assignment 2
Risky Business
Student Name: YOUR NAME
Date started: YYYY-MM-DD

Pseudocode:

CONSERVATIVE_CHANCE = 68
CONSERVATIVE_REWARD = 0.24
AGGRESSIVE_CHANCE = 42
AGGRESSIVE_REWARD = 0.64
CRAZY_CHANCE = 7
CRAZY_REWARD = 1.44
STARTING_BALANCE = 1248.48

function main()
    print "Welcome to Risky Business"
    set balance to STARTING_BALANCE
    create empty list called results

    call display_menu
    set choice to get_valid_menu_choice()

    while choice is not "Q"
        if choice is "P"
            if balance is less than or equal to 0
                print "You have no $$$... time to quit!"
            else
                set result, balance to play_turn(balance)
                append result to results
        else if choice is "I"
            call display_instructions
        else if choice is "D"
            if results is empty
                print "No risks taken yet. Get started..."
            else
                call display_report(results, STARTING_BALANCE)
        else if choice is "S"
            if results is empty
                print "No risks taken, so there are no statistics."
            else
                call display_statistics(results)
        else
            print "Invalid choice"

        call display_menu
        set choice to get_valid_menu_choice()

    call display_summary(results, STARTING_BALANCE)
    ask user "Save your results to a file? (Y)es or (N)o?"
    if user input is not "N"
        call save_results_to_file(results)
        print "Results saved."
    print "Thank you for playing Risky Business."

function play_turn(balance)
    ask user "Enter amount to risk, up to $balance:"
    set risk_amount to get_valid_risk_amount(balance)
    ask user "(C)onservative, (A)ggressive, Cra(Z)y:"
    set risk_level to get_valid_risk_level()

    generate random_number between 1 and 100

    if risk_level is "C"
        set chance to CONSERVATIVE_CHANCE
        set reward_multiplier to CONSERVATIVE_REWARD
    else if risk_level is "A"
        set chance to AGGRESSIVE_CHANCE
        set reward_multiplier to AGGRESSIVE_REWARD
    else
        set chance to CRAZY_CHANCE
        set reward_multiplier to CRAZY_REWARD

    if random_number is less than or equal to chance
        set reward to risk_amount × reward_multiplier
        add reward to balance
        round balance to 2 decimal places
        print "Congratulations! You earned $reward"
        return reward, balance
    else
        subtract risk_amount from balance
        round balance to 2 decimal places
        print "You lost $risk_amount"
        set loss to negative risk_amount
        return loss, balance
"""

import random

CONSERVATIVE_CHANCE = 68
CONSERVATIVE_REWARD = 0.24
AGGRESSIVE_CHANCE = 42
AGGRESSIVE_REWARD = 0.64
CRAZY_CHANCE = 7
CRAZY_REWARD = 1.44
STARTING_BALANCE = 1248.48


def main():
    """Main function to run the Risky Business game."""
    print("Welcome to Risky Business")
    balance = STARTING_BALANCE
    results = []

    display_menu()
    choice = get_valid_menu_choice()

    while choice != "Q":
        if choice == "P":
            if balance <= 0:
                print("You have no $$$... time to quit!")
            else:
                result, balance = play_turn(balance)
                results.append(result)
        elif choice == "I":
            display_instructions()
        elif choice == "D":
            if not results:
                print("No risks taken yet. Get started...")
            else:
                display_report(results, STARTING_BALANCE)
        elif choice == "S":
            if not results:
                print("No risks taken, so there are no statistics.")
            else:
                display_statistics(results)
        else:
            print("Invalid choice")

        display_menu()
        choice = get_valid_menu_choice()

    display_report(results, STARTING_BALANCE)
    save_choice = input("Save your results to a file? (Y)es or (N)o? ").strip().lower()
    if save_choice != "n":
        save_results_to_file(results)
        print("Results saved.")
    print("Thank you for playing Risky Business.")


def display_menu():
    """Display the main menu."""
    print("(P)lay (I)nstructions (D)isplay Report (S)tatistics (Q)uit")


def get_valid_menu_choice():
    """Get a valid menu option from the user."""
    choice = input("Choose: ").strip().upper()
    return choice


def display_instructions():
    """Display the game instructions."""
    print("Risky Business")
    print("Each turn, you can risk some of your cash to try and win a reward.")
    print("You can choose a risk level:")
    print("- conservative (68% chance for a +24% reward)")
    print("- aggressive (42% chance for a +64% reward)")
    print("- crazy (7% chance for a +144% reward)")
    print("If your risk-taking doesn't pay off, you lose the amount you choose to risk.")
    print("Risky Business. You win some. You lose more.")


def get_valid_risk_amount(balance):
    """Prompt user for a valid risk amount."""
    while True:
        try:
            amount = float(input(f"Enter amount to risk, up to ${balance:.2f}: $"))
            if 0 < amount <= balance:
                return round(amount, 2)
            else:
                print("You can't risk that amount!")
        except ValueError:
            print("Invalid input; please enter a number.")


def get_valid_risk_level():
    """Prompt user for a valid risk level."""
    while True:
        risk_level = input("(C)onservative, (A)ggressive, Cra(Z)y: ").strip().upper()
        if risk_level in ["C", "A", "Z"]:
            return risk_level
        else:
            print("Please choose from the available options.")


def play_turn(balance):
    """Play a single game turn."""
    risk_amount = get_valid_risk_amount(balance)
    risk_level = get_valid_risk_level()
    roll = random.randint(1, 100)

    if risk_level == "C":
        chance = CONSERVATIVE_CHANCE
        reward_rate = CONSERVATIVE_REWARD
    elif risk_level == "A":
        chance = AGGRESSIVE_CHANCE
        reward_rate = AGGRESSIVE_REWARD
    else:
        chance = CRAZY_CHANCE
        reward_rate = CRAZY_REWARD

    if roll <= chance:
        reward = round(risk_amount * reward_rate, 2)
        balance += reward
        balance = round(balance, 2)
        print(f"Congratulations! You earned ${reward:.2f}")
        return reward, balance
    else:
        balance -= risk_amount
        balance = round(balance, 2)
        print(f"You lost ${risk_amount:.2f}")
        return -risk_amount, balance


def display_report(results, starting_balance):
    """Display the report of all results."""
    balance = starting_balance
    print("Risky Results Report:")
    print(f"Starting balance: ${starting_balance:.2f}")
    for result in results:
        balance += result
        print(f"${result:9.2f}  ->  ${balance:9.2f}")
    print(f"Current balance:${balance:10.2f}")


def display_statistics(results):
    """Display statistics about results."""
    wins = [r for r in results if r > 0]
    losses = [r for r in results if r < 0]
    print(f"Best result : ${max(results):.2f}")
    print(f"Worst result: ${min(results):.2f}")
    total = len(results)
    win_percent = len(wins) / total * 100
    loss_percent = len(losses) / total * 100
    print(f"{win_percent:6.1f}% ({len(wins)}/{total}) of your turns were gains")
    print(f"{loss_percent:6.1f}% ({len(losses)}/{total}) of your turns were losses")


def save_results_to_file(results):
    """Save results to a file called results.txt"""
    with open("results.txt", "w") as file:
        for result in results:
            file.write(f"{result}\n")


main()
