from art import *
from data import data
import random
import os

def play_game():
    def pick_random_data():
        """Returns a random data from the list of data"""
        return random.choice(data)

    a = pick_random_data()
    b = pick_random_data()
    
    score = 0
    game_over = False
    print(logo)

    # {
        # 'name': 'Kourtney Kardashian', 
        # 'follower_count': 90, 
        # 'description': 'Reality TV personality', 
        # 'country': 'United States'
        # }

    # {
        # 'name': 'Rihanna', 
        # 'follower_count': 81, 
        # 'description': 'Musician and businesswoman', 
        # 'country': 'Barbados'
        # }


    while not game_over:
        if a == b :
            b = pick_random_data()
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
        user_choice = input("Who has more followers? Type 'A' or 'B': ").capitalize()

        if a["follower_count"] > b["follower_count"] and user_choice == "A":
            a = b
            b = pick_random_data()
            score += 1
            os.system('clear')
            print(logo)
            print(f"You are right, current score is {score}")
        elif b["follower_count"] > a["follower_count"] and user_choice == "B":
            a = b
            b = random.choice(data)
            score += 1
            os.system('clear')
            print(logo)
            print(f"You are right, current score is {score}")
        else:
            os.system('clear')
            print(f"Sorry that's wrong final score is: {score}")
            game_over = True


play_game()