############### Blackjack Project #####################
import random
from replit import clear
from art import logo

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    index = random.randint(0,12)
    return index

def calculate_score(list):
    total = 0
    total = sum(list)
    if len(list) == 2 and 11 in list and 10 in list:
        return 0
    if 11 in list:
        if total > 21:
            list.remove(11)
            list.append(1)
            total = sum(list)
    return total

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Its draw"
    elif computer_score == 0:
        return "BlackJack! Computer wins"
    elif user_score == 0:
        return "BlackJack! User wins"
    elif user_score > 21:
        return "Computer wins"
    elif computer_score > 21:
        return "User wins"
    elif computer_score > user_score:
        return "Computer wins"
    elif user_score > computer_score:
        return "User wins"

start = input("Do you want to start new game? y/n: ")

def game():
    user_cards = []
    computer_cards = []
    print(logo)
    user_cards.append(cards[deal_card()])
    user_cards.append(cards[deal_card()])
    computer_cards.append(cards[deal_card()])
    computer_cards.append(cards[deal_card()])

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    while True:



        if user_score == 0 or computer_score > 21:
            print("User wins")
            break
        elif computer_score == 0 or user_score > 21:
            print("Computer wins")
            break
        else:
            question = input("Type 'y' to get another card, type 'n' to pass:")
            if question == 'y':
                user_cards.append(cards[deal_card()])
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")

            elif question == 'n':
                while computer_score < 17:
                    computer_cards.append(cards[deal_card()])
                    computer_score = calculate_score(computer_cards)
                    print(f"Your final cards: {user_cards}, final score: {user_score}")
                    print(f"Computer final cards: {computer_cards}, final_score: {computer_score}")
                    compare(user_score,computer_score)
                    if input("Do you want to start new game? y/n: ") == 'y':
                        clear()
                        game()
                    else:
                        break
game()