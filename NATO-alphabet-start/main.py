import pandas

with open("nato_phonetic_alphabet.csv") as file:
    f = pandas.read_csv(file)
    df = pandas.DataFrame(f)

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate():
    try:
        user_word = input("Enter your word: ").upper()
        nato_user_word = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Enter alphabet only.")
        generate()
    else:
        print(nato_user_word)


generate()
