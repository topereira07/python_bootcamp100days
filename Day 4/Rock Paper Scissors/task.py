import random

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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Papel and 2 for Scissors\n"))
print(f"You chose: {choice}")
options = [rock, paper, scissors]
computer = random.randint(0,2)
if choice == 0:
    print(rock)
    print("Computer chose:")
    print(options[computer])
    if computer == 1:
        print("You lose")
    elif computer == 2:
        print("You win")
    else:
        print("It's a tie")
elif choice == 1:
    print(paper)
    print("Computer chose:")
    print(options[computer])
    if computer == 0:
        print("You win")
    elif computer == 2:
        print("You lose")
    else:
        print("It's a tie")
elif choice == 2:
    print(scissors)
    print("Computer chose:")
    print(options[computer])
    if computer == 0:
        print("You lose")
    elif computer == 1:
        print("You win")
    else:
        print("It's a tie")
else:
    print("You lose because you did not type a correct option!!")

