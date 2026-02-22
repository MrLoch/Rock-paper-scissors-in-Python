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

options = [rock, paper, scissors] # Creating a list of possible options

# Ask the player what their choice is
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Import random choice for computer
import random

computer_choice = (random.choice(options))

# The rock option
if player_choice == 0:
    print(options[0])
    print("Computer chose:\n" + computer_choice)
    if computer_choice == options[0]:
        print("It's a draw!")
    elif computer_choice == options[1]:
        print("You lose!")
    else:
        print("You win!")

# The paper option
elif player_choice == 1:
    print(options[1])
    print("Computer chose:\n" + computer_choice)
    if computer_choice == options[0]:
        print("You win!")
    elif computer_choice == options[1]:
        print("It's a draw!")
    else:
        print("You lose!")

# The scissors option
elif player_choice == 2:
    print(options[2])
    print("Computer chose:\n" + computer_choice)
    if computer_choice == options[0]:
        print("You lose!")
    elif computer_choice == options[1]:
        print("You win!")
    else:
        print("It's a draw!")

else:
    print("That is not a valid input.")
