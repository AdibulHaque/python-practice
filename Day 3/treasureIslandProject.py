"""Your goal today is to build a "Chose your own adventure game•. Using what
you have learnt in the lessons today you will be building a very simple version
of this type of text game.
Use the flow chart linked here https://tinyurl.com/3fum685t to create the game logic.
Once you,ve completed the project, you can always extend the game and make
it more interesting! """

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
choice1 = input("      Type \"left\" or \"right\"\n").lower()
if choice1 == "left":
    print("You 've come to a lake.There is an island in the middle of the lake.")
    choice2 = input("      Type \"wait\" to wait for a boat or \"swim\" to swim across\n").lower()
    if choice2 == "wait":
        print("You arrive at the island unharmed.There is a house with 3 doors.")
        choice3 = input("      One Red one Yellow and one Blue. Which colour do you choose?").strip().capitalize()
        if choice3 == "Red":
            print("Burned by fire. Game Over.")
        elif choice3 == "Blue":
            print("Eaten by beasts. Game Over.")
        elif choice3 == "Yellow":
            print("You found the treasure! You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole.Game Over")




