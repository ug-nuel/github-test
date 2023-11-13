from ceasar_art import logo

print(logo)


# adding both the encrypt and decrypt funtions together
def caesar(start_text, shift_amt, cipher_direction):
    global new_position
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amt
            elif cipher_direction == "decode":
                new_position = position - shift_amt
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"the {cipher_direction}d text is {end_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # this allows you to put any number for the shift amount and get a result regardless cause its
    # cutting the number down to fit with the number of alphabets we have

    caesar(start_text=text, shift_amt=shift, cipher_direction=direction)
    result = input("type 'yes' if you want to go again. otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("bye bye")


# doing it one at a time
# def encrypt(plain_text, shift_amt):
#     cipher_text = " "
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amt
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the encoded text is {cipher_text}")
#
#
# def decrypt(cipher_text, shift_amt):
#     plain_text = " "
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amt
#         plain_text += alphabet[new_position]
#     print(f"the decoded text is {plain_text}")
#
#
# if direction == 'encode':
#     encrypt(plain_text=text, shift_amt=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_amt=shift)
