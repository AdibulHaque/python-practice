# Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

def  information(b,a):
    print(f"Hello {b}")
    print(f"What is it like in {a}")

name = input("Input name: ")
location = input("Input Location: ")

information(a = location,b = name) #Keyword argument