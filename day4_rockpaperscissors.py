import random

print("What do you choose?")
user_input=input("Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
user_input=int(user_input)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if user_input == 0 :
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)
else:
    print ("Your input is wrong!")

computer_choose = random.randint(0,2)
print("Computer chose:")
if computer_choose == 0 :
    print(rock)
elif computer_choose == 1:
    print(paper)
elif computer_choose== 2:
    print(scissors)

if user_input == computer_choose:
    print("Draw")
elif user_input == 0 and computer_choose == 1:  # rock vs paper
    print ("You lose")
elif user_input == 0 and computer_choose == 2 :  # rock vs scissors
    print ("You win")
elif user_input == 1 and computer_choose == 0 :  # paper vs rock
    print ("You win")
elif user_input == 1 and computer_choose == 2 :  # paper vs scissors
    print ("You lose")
elif user_input == 2 and computer_choose == 0 :  # scissor vs rock
    print ("You lose")
elif user_input == 2 and computer_choose == 1 :  # scissor vs paper
    print ("You win")

else:
    print("Error please try again")
