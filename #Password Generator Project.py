#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_letters = ''
password_symbols = ''
password_numbers = ''
password_letters_list = random.sample(letters, k=nr_letters)
password_symbols_list = random.sample(symbols, k=nr_symbols)
password_numbers_list = random.sample(numbers, k=nr_numbers)
# password_list = password_letters_list + password_numbers_list + password_symbols_list
# print(password_list)
# password = random.shuffle(password_list)
# print(password)
for letter in password_letters_list:
    password_letters = password_letters + letter
for symbol in password_symbols_list:
    password_symbols = password_symbols + symbol
for number in password_numbers_list:
    password_numbers = password_numbers + number

password = password_letters + password_numbers + password_symbols
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Convert string to a list of characters
char_list = list(password)
    
# Shuffle the list of characters
random.shuffle(char_list)
    
# Convert the list of characters back into a string
shuffled_string = ''.join(char_list)
print(shuffled_string)