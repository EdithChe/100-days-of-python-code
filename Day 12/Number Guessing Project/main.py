import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
list_of_numbers = [i for i in range(1, 101)]
number = random.choice(list_of_numbers)


def play_game():

    if difficulty == 'easy':
        attempts = 10
    if difficulty == 'hard':
        attempts = 5

    is_game_over = False
    while not is_game_over:
        guess = int(input("Make a guess: "))
        if guess == number:
            is_game_over = True
            print(f"You got it! The answer was {number}")
        else:
            attempts -= 1
            if attempts == 0:
                is_game_over = True
                print("You've run out of guesses. You lose.")
            else:
                if guess < number:

                    print("Too low. Guess again.")
                elif guess > number:
                    attempts -= 1
                    print("Too high. Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number:")

play_game()


