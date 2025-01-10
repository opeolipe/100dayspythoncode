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

print('You are on the boat and you see a harbour. '
      'Where do you want to go?')
first_step = input('Type "harbour" to go to the harbour. '
                   'Type "sail" to keep on sailing.\n').lower()
if first_step == "harbour":
    print("You go off from the boat and meet a beautiful person. "
          "Do you want to talk with her?")
    second_step = input('Type "flirt" to talk with her. '
                        'Type "ignore" to go to a house.\n').lower()
    if second_step == "flirt":
        third_step = input ('Because you have a good charm. She give you something. '
                            'Do you want to accept it? \n Type "yes" to accept. '
                            'Type "no" to ignore.\n').lower()
        if third_step == "yes" :
            print ("You open the box and meet Ikara! "
                   "Congratulation you meet a treasure, IKARA!")
        elif third_step == "no":
            print ("She is mad a you, and stab you heart! You die")
        else:
            print("Game over. You die!")
    elif second_step == "ignore":
        print("You went to a house and meet bunch of bandits. "
              "They shoot you and you die.")
    else:
        print("Game over. You die!")
elif first_step == "sail":
    print ("Game over, you die in a storm")
else:
    print("Game over. You die!")
