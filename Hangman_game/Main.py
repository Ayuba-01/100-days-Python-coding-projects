
import random
import os
from hangman_art import *
from hangman_words import *


end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
live = 7

print (logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  os.system('clear')
  
  if guess in display:
    print(f"You already guessed letter '{guess}'.")
  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
        display[position] = letter
  
  

  if not guess in chosen_word:
    print(f"You guessed the letter '{guess}', that's not in the word, you loose a life. Try again")
    live = live - 1
    print(stages[live])
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("You win.")
  elif live == 0:
    end_of_game = True
    print("You loss!")
    