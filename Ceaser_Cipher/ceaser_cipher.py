from Ceaser_ciper_logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(input_text, shifts_number, cipher_direction):
    final_text = ""
    if cipher_direction != "encode" or direction != "decode":
            print("You didn't type encode or decode.")
    for char in input_text:
        if char in alphabet: 
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shifts_number
            elif direction == "decode":
                new_position = position - shifts_number
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"The {cipher_direction}d text is {final_text}")



print (logo)
end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    ceaser(text, shift, direction)
    answer = input("Type 'yes' to continue or 'no' to stop: ").lower()
    if answer == "no":
        end = True
        print ("Good Bye")







    
    


