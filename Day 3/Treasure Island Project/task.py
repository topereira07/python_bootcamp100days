print('''
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
cross_road = input('  Type "left" or "right"\n').lower()
if cross_road != "left":
    print("Game Over! You felt into a hole...")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    option1 = input('  Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if option1 != "wait":
        print("Game Over! You were attacked by a trout...")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        option2 = input("  One red, one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if option2 == "red":
            print("Game Over! You were burned by fire..")
        elif option2 == "blue":
            print("Game over! You were eaten by beasts..")
        elif option2 != "yellow":
            print("Game over!!!")
        else: print("You've found the treasure! You WIN.. Congratulations!")