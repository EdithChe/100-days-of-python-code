from art import logo, vs
from game_data import data
import random
print(logo)


celebrities = [celebrity for celebrity in data]


#Compare artist a with artist b


def format_data(celebrity):
    celebrity_name = celebrity["name"]
    celebrity_description = celebrity["description"]
    celebrity_country = celebrity["country"]
    return f"{celebrity_name}, a {celebrity_description}, from {celebrity_country}"

def play_game():
    score = 0
    is_game_over = False

    celebrity_b = random.choice(celebrities)
    # if guess is correct, score increments and artist with the least amount of followers becomes 'a', and new artist becomes b
    while not is_game_over:
        celebrity_a = celebrity_b
        celebrity_b = random.choice(celebrities)

        if celebrity_a == celebrity_b:
            celebrity_b = random.choice(celebrities)

        print(f"Compare A: {format_data(celebrity_a)}.")
        print(vs)
        print(f"Against B: {format_data(celebrity_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        if (celebrity_a['follower_count'] > celebrity_b['follower_count'] and guess == 'A') or (celebrity_a['follower_count'] < celebrity_b['follower_count'] and guess == 'B'):
            score +=1

            print(f"You're right! Current score: {score}.")

        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}.")

# game continues until guess is incorrect



play_game()


