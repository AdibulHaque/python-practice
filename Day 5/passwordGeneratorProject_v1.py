# Easy Version
# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants
# 4 letters 2 symbols and 3 numbers then the password might look like this:fgdx$*924
# You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

new_list = []
for new_letters in range(nr_letters):
    random_letters = (random.choice(letters))
    new_list.append(random_letters)

for new_symbols in range(nr_symbols):
    random_symbols = (random.choice(symbols))
    new_list.append(random_symbols)

for new_numbers in range(nr_numbers):
    random_numbers = (random.choice(numbers))
    new_list.append(random_numbers)
print(new_list)

print("Your password is: " + "".join(new_list))