import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
        if char in alphabet:
            print(f"Here's the {cipher_direction}d result: {end_text}", end="")
        else:
            print(f"Here's the {cipher_direction}d result: {char}",
                  end="")
            print()


print(art.logo)
p = True
while p:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        shift %= 25
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    a = input("enter y to continue or n to exit")
    if a == 'y':
        p = True
    else:
        p = False
if not p:
    print("Goodbyee")
