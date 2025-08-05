alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

def encrypt(original_text,shift_amount):
    new_msg = []
    # new_msg_string = " " We can also do by empy string
    for char in original_text:
        shifted_alphabet_position = alphabet.index(char) + shift_amount
        # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
        # if shifted_alphabet_position >= 26:
        #     shifted_alphabet_position = shifted_alphabet_position % 26
        shifted_alphabet_position %= len(alphabet)
        shifted_alphabet = alphabet[shifted_alphabet_position]
        #new_msg_string += alphabet[Shifted_alphabet_position]
        new_msg.append(shifted_alphabet)
    print("Your encoded Code is: " , *new_msg, sep='')

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
if direction == 'encode':
    encrypt(original_text=text,shift_amount=shift)
elif direction == 'decode':
    print("Decode feature is not ready")
else:
    print("Wrong Input")