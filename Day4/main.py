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

choices = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

computer_choice = random.randint(0, len(choices)-1)

if player_choice < 3 and player_choice >= 0:
    print(choices[player_choice])
    print("Computer chose: \n" + choices[computer_choice])

    if player_choice == computer_choice:
        print("It's a Draw!")

    if player_choice == 0:
        if computer_choice == 1:
            print("Sorry, you lose.")
        elif computer_choice == 2:
            print("Congratulations, you win!")
    elif player_choice == 1:
        if computer_choice == 0:
            print("Congratulations, you win!")
        elif computer_choice == 2:
            print("Sorry, you lose.")
    elif player_choice == 2:
        if computer_choice == 0:
            print("Sorry, you lose.")
        elif computer_choice == 1:
            print("Congratulations, you win!")
else:
    print("You typed an invalid choice. Enter 0, 1, or 2.")
