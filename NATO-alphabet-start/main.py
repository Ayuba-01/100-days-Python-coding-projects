import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

with open("nato_phonetic_alphabet.csv") as file:
    f = pandas.read_csv(file)
    df = pandas.DataFrame(f)

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
user_word = input("Enter your word: ").upper()
nato_user_word = [nato_dict[letter] for letter in user_word if letter in nato_dict.keys()]
print(nato_user_word)


