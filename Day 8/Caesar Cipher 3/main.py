# TODO-1: Import and print the logo from art.py when the program starts.
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
            continue
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

def restart(new_direction, new_text, new_shift):
    start = input("Do you want to go again? Types 'yes' or 'no'..")
    if start == "yes":
        new_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        new_text = input("Type your message:\n").lower()
        new_shift = int(input("Type the shift number:\n"))
        caesar(original_text=new_text, shift_amount=new_shift, encode_or_decode=new_direction)
    elif start == "no":
        quit()
    else:
        print("Please choose the correct option!")
        restart(new_direction, new_text, new_shift)
    restart(new_direction,new_text,new_shift)
restart(new_text=text, new_shift=shift, new_direction=direction)

