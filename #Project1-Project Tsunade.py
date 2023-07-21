# text Base slot machine
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line+1)
    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # [:] is a slice operator
        for _ in range(rows):
            value = random.choice(current_symbols)  # picks a random value from the list
            current_symbols.remove(value)  # makes sure that we don't pick the same value again
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


# this function is responsible for collecting the user input that gets the deposit from the user
# function for deposit amount
def deposit():
    # why while loop??-asking user continuously until a valid amount is given as input
    while True:
        amount = input("What would you like to deposit?? ")
        if amount.isdigit():  # "isdigit()" function is used to check if given input is a digit or not
            amount = int(amount)  # By default, the input is in string from, so it is converted to "int"
            if amount > 0:
                break  # if they did enter a number>0,break out of the while loop
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number: ")  # if they did not enter a number then it is printed out
    return amount


# function for number of lines
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines: ")
        else:
            print("Please enter a number: ")
    return lines


# function getting user input for bet
def get_bet():
    while True:
        amount = input("What would you like to bet on each line?? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    f"Amount must be between {MIN_BET} - {MAX_BET}")  # f string is used to concatenate the  variables
                # inside a print function
        else:
            print("Please enter a number: ")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:  # condition is given because if the user is betting more than their balance
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You dont have enough balance to bet. Your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winnings_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)


main()
