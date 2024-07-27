############### Blackjack Project #####################
import random
import os
from black_jack_art import logo

def deal_card():
    """Return a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculate player and dealer score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(u_score, c_score):
    """Compare player and dealer score"""
    if u_score > 21:
        return f"Your Score: {u_score}\nDealer Score: {c_score}\nYou lose!"
    elif c_score > 21:
        return f"Your Score: {u_score}\nDealer Score: {c_score}\nYou win!"
    elif c_score == 0:
        return f"Dealer has a blackjack, you lose!"
    elif u_score == 0:
        return f"You have a blackjack, you wins!"
    elif u_score == c_score:
        return f"Your Score: {u_score}\nDealer Score: {c_score}\nThe game is a draw!"
    elif u_score > c_score:
        return f"Your Score: {u_score}\nDealer Score: {c_score}\nYou win!"
    elif c_score > u_score:
        return f"Your Score: {u_score}\nDealer Score: {c_score}\nYou lose!"


def play_game():
    """Play Black Jack Game"""
    print(logo)
    game_over = False
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User cards: {user_cards}, Current Score: {user_score}")
        print(f"Dealer First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_input = input("Would you like to deal another card ? Type 'y' for Yes and 'n' for No: ").lower()
            if user_input == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
                

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand is {user_cards}\nDealer final hand is {computer_cards}")
    print(compare(user_score, computer_score))
      
while input("Do you want to play Black Jack Game? Type 'y' for 'Yes' and 'n' for 'No': ").lower() == 'y':
    os.system('clear')
    play_game()
    