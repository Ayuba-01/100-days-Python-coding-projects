alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(text, shifts, direction):
    final_text = ""
    if direction != "encode" or direction != "decode":
            print("You didn't type encode or decode.")
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shifts
        elif direction == "decode":
            new_position = position - shifts
        final_text += alphabet[new_position]
    print(f"The {direction}d text is {final_text}")


ceaser(text, shift, direction)

    
    


