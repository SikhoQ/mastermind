"""
TODO:   (1) Add functionality to display previous guess
            after having entered invalid input
        (2) Add functionality to disallow digit repeats
            in generated code
"""

from random import randint


def generate_code():
    return [randint(2, 8) for i in range(4)]


def print_welcome():
    print("\n\nWelcome to Mastermind")
    print("A 4-digit code of digits 2-8 has been set.")
    print("You have 5 turns to guess the correct code. Good luck!")


def guess_code():
    guess = input("\nGuess the code: ")
    while not valid_input(guess):
        guess = input("Guess the code: ")
    return [int(digit) for digit in guess]


def valid_input(guess):
    if len(guess) != 4:
        print("\nInvalid input. Must be 4 digits between 2-8 inclusive.")
        return False
    for c in guess:
        if not c.isdigit():
            print("\nInvalid input. Must only be digits.")
            return False
        if int(c) < 2 or int(c) > 8:
            print("\nInvalid input. Digits must be between 2-8 inclusive.")
            return False
    return True


def correct_digits_correct_place(user_code, code):
    print("\nNumber of correct digits in the correct place: ", end='')
    print(sum([1 for i in range(4) if user_code[i] == code[i]]))


def correct_digits_incorrect_place(user_code, code):
    count = 0
    for i in range(4):
        if user_code[i] in code and user_code[i] != code[i]:
            count += 1
    print(f"Number of correct digits NOT in correct place: {count}")


def run_game():
    code = generate_code()
    print_welcome()
    user_code = guess_code()
    turns = 1

    while code != user_code and turns != 5:
        correct_digits_correct_place(user_code, code)
        correct_digits_incorrect_place(user_code, code)
        print(f"You have {5-turns} ", end='')
        print("turns left.") if turns < 4 else print("turn left.")
        user_code = guess_code()
        turns += 1
    if code == user_code:
        print(f"{''.join([str(n) for n in user_code])} You win!")
    else:
        print("You ran out of turns. ", end='')
        print(f"The code was {''.join([str(n) for n in code])}.")


if __name__ == "__main__":
    run_game()
