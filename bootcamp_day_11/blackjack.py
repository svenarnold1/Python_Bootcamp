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


def black_jack():
    # value of cards available
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    dealer = []


    def user_draw():
        # give user random card
        user_cards.append(random.choice(cards))


    def dealer_draw():
        # give dealer random card
        dealer.append(random.choice(cards))


    def score(card_values):
        score = 0
        for card in card_values:
            is_ace = (card == 11)
            score += card
            if is_ace and score > 21:  # Ace can represent 11 or 1
                card_values[card_values.index(11)] = 1
        return score


    def winner(user, computer):
        if user == 21:
            return "Blackjack! You won!"
        elif user > 21:
            return "Bust! You Lost!"
        elif dealer == computer:
            return "Tie"
        elif (user > computer) and (user <= 21) or computer > 21:
            return "You won!"
        else:
            return "Dealer won!"


    def dealer_hand(computer):
        while computer < 17:
            dealer_draw()
            computer = score(dealer)
        return computer



    # give user and dealer one card
    user_draw()
    dealer_draw()

    should_continue = True
    while should_continue:
        # give user a card
        user_draw()
        # store score of player
        user_score = score(user_cards)
        dealer_score = score(dealer)
        if user_score > 21:
            dealer_hand(computer=dealer_score)
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Dealers hand: {dealer}, Dealer score: {dealer_score}")
            print(winner(user=user_score, computer=dealer_score))
            break
        else:
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Dealers first card: {dealer}")
            if input(f"Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
                continue
            else:
                should_continue = False
                dealer_score = dealer_hand(computer=dealer_score)
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Dealers hand: {dealer}, Dealer score: {dealer_score}")
                print(winner(user=user_score, computer=dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print(logo)
    black_jack()



