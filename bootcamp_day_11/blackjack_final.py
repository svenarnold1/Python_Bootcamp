# This is a simple blackjack game
from blackjack_art import logo
import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.


def deal_card():
    """Deals random cards of deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_values):
    """Take a list of cards and return score of values in list"""
    if sum(card_values) == 21 and len(card_values) == 2:
        return 0

    elif 11 in card_values and sum(card_values) > 21:
        card_values.remove(11)
        card_values.append(1)

    return sum(card_values)


def winner(user, computer):
    """determines who has won the game"""
    if user == 0:
        return "Blackjack! You won!"
    elif computer == 0:
        return "You lost, opponent has a Blackjack!"
    elif user > 21:
        return "Bust! You Lost!"
    elif user == computer:
        return "draw"
    elif (user > computer) and (user <= 21) or computer > 21:
        return "You won!"
    else:
        return "Dealer won, you loose!"


def play_game():
    print(logo)
    user_cards = []
    dealer_cards = []
    is_game_over = False
    dealer_score = 1
    user_score = 1

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealers first card: {dealer_cards}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        elif input(f"Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your cards: {user_cards}, final score: {user_score}")
    print(f"Dealers cards: {dealer_score}, final score: {dealer_score}")
    print(winner(user_score, dealer_score))


# ask user if game should restart and restart if wanted
while input("Do you want to play a game of blackjack? Type 'y' or 'n':\n").lower() == 'y':
    print("\n"*10)
    play_game()

