import random
from art import logo


def play_game():
    print(logo)
    print("Welcome to Guess the Number")
    rand_num = random.randint(1,100)
    print("I am thinking of a number from 1 to 100")
    attempts = -1
    game_over = False

    level = input("Choose level. Type 'easy', 'medium' or 'hard': ").lower()
    if level == "easy":
        attempts = 10
    elif level == "medium":
        attempts = 7
    elif level == "hard":
        attempts = 5
    else:
        print("Run again and Enter a valid level")
    print(f"You have chosen {level} level, you have {attempts} attempts left.")
        
    while not game_over:
        player_guess = int(input("Guess a number: "))
        if player_guess > rand_num:
            print("Too high")
            attempts = attempts - 1
            print(f"You have {attempts} attempts left.")
        elif player_guess < rand_num:
            print("Too low")
            attempts = attempts - 1
            print(f"You have {attempts} attempts left.")
        else:
            print(f"Congratulations you guessed rigth, the number is {rand_num}")
            game_over = True
            
        if attempts == 0:
            print("You don't have any attempts left. Game Over ")
            game_over = True


play_game()
