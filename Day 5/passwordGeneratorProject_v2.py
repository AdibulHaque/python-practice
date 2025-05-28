# Hard Version
# When you've completed the easy version, 
# you're ready to tackle the hard version. 
# In the advanced version of this project the final 
# password does not follow a pattern.
#  So the example above might look like this:x$d24g*f
# And every time you generate a password,
#  the positions of the symbols, numbers,
#  and letters are different. 
# This will make the password more difficult for hackers to crack.



import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

new_list1 = []
for new_letters in range(nr_letters):
    random_letters = (random.choice(letters))
    new_list1.append(random_letters)
new_list2 = []
for new_symbols in range(nr_symbols):
    random_symbols = (random.choice(symbols))
    new_list2.append(random_symbols)
new_list3 = []
for new_numbers in range(nr_numbers):
    random_numbers = (random.choice(numbers))
    new_list3.append(random_numbers)
combined = new_list1 + new_list2 + new_list3
random.shuffle(combined)
print("Your password is: " + "".join(combined))
