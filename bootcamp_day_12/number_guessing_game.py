import random
from art import logo

# choose number between 1 and 100
# difficulties = easy or hard. easy has 10 attemps, hard has 5
# pick random number
# user has to guess.. response to high or to low depending on what is true

# fill the number list with numbers from 1 - 100
number = []
for num in range(1, 101):
    number.append(num)


# pick random number out of number list
def pick_num():
    return random.choice(number)


secret_num = pick_num()
print(secret_num)

def define_lives():
    global lives
    print(logo)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

    if difficulty == 'hard':
        lives = 5
    elif difficulty == 'easy':
        lives = 10
    else:
        print("invalid input!")
        lives = 0
    return lives


# assign levels depending on difficulty
lives = define_lives()


def play_game(secret):
    print(secret)
    # ask user what difficulty should be set
    print("I'm thinking of a number between 1 and 100.")

    guessed_num = 0

    def guess_num():
        global lives
        if guessed_num > secret:
            lives -= 1
            if lives > 0:
                return "To high \nGuess again"
            else:
                return "To high \nYou lost"
        elif guessed_num < secret:
            lives -= 1
            if lives > 0:
                return "To low \nGuess again"
            else:
                return "To low \nYou lost"
        else:
            return f"You got it! The answer was {secret}"

    while guessed_num != secret and lives > 0:
        # ask user to guess an number
        print(f"You have {lives} attempts remaining to guess the number.")
        guessed_num = int(input("Make a guess: "))
        print(guess_num())

    if (guessed_num == secret or lives == 0) and input(f"Type 'y' to play again").lower() == 'y':
        define_lives()
        play_game(pick_num())
    else:
        print("See you next time!")


play_game(secret_num)
# Eof (End of File)
