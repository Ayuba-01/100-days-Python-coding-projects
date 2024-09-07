# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()
    print(name_list)


with open("./Input/Letters/starting_letter.txt", "r") as letter:
    l = letter.read()
    for name in name_list:
        clear_name = name.strip()
        replaced_letter = (l.replace("[name]", f"{clear_name}"))
        with open(f"./Output/ReadyToSend/letter_for_{clear_name}.txt", "w") as new_letter:
            new_letter.write(f"{replaced_letter}")


