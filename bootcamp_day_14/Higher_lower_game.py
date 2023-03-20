from game_data import data
from art import logo, vs
import random


vowels = "AEIOUaeiou"


def random_choice():
    return random.choice(data)


def compare(follower_a, follower_b):
    if follower_a['follower_count'] > follower_b['follower_count']:
        return 1
    else:
        return 0


score = 0
person_a = random_choice()
person_b = random_choice()


def play_game():
    global score, person_a, person_b
    # check if random choice is same and change person b if so.
    if person_a == person_b:
        person_b = random_choice()
    keep_going = True
    while keep_going:
        print(logo)
        if score >= 1:
            print(f" You're Right! Current score: {score}")
        # decide if 'a' or 'an'
        if person_a['description'][0] in vowels:
            print(f"Compare A: {person_a['name']}, an {person_a['description']}, from {person_a['country']}")
        else:
            print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
        print(vs)
        # decide if 'a' or 'an'
        if person_b['description'][0] in vowels:
            print(f"Against B: {person_b['name']}, an {person_b['description']}, from {person_b['country']}")
        else:
            print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if guess == 'A' and compare(person_a, person_b) == 1 or guess == 'B' and compare(person_a, person_b) == 0:
            score += 1
            person_a = person_b
            person_b = random_choice()
        else:
            keep_going = False
            print(f"Sorry, that's wrong. Final score: {score}")


play_game()

# Eof (End of File)
