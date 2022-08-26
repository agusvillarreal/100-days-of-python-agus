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

game_images = [rock, paper, scissors]
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print('Your chose:')
if user >= 3 or user < 0:
    print('Invalid number, you lose')
else:
    print(game_images[user])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    elif user == 0 and computer_choice == 2:
        print('You win')
    elif computer_choice == 0 and user == 2:
        print('You lose')
    elif computer_choice > user:
        print('You lose')
    elif user > computer_choice:
        print('You win')
    elif computer_choice == user:
        print('Draw')
