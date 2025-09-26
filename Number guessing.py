
#                 >>> NUMBER GUESSING PROGRAM <<<
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Welcome To Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess:")

    if guess.isdigit():
        guess = int(guess)
        guesses = guesses + 1

        if guess <= lowest_num and guess >= highest_num:
            print("that number is out of range..")
            print(f"Select a number between {lowest_num} and {highest_num}")

        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print("-------------------------------")
            print(f"CORRECT! The answer is {answer}")
            print(f"Number of guesses: {guesses}")
            print("-------------------------------")
            is_running = False
    else:
        print("Invalid guess...")
        print(f"Select a number between {lowest_num} and {highest_num}")
