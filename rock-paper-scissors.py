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

game_art = [rock, paper, scissors]

print("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS.")
choice = int(input())

if choice > 2 or choice < 0:
    print("Invalid input!")
else:
    print(game_art[choice])

    ai_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_art[ai_choice])

    if choice == ai_choice:
        print("Draw")
    elif choice == 0 and ai_choice == 1:
        print("You lose")
    elif choice == 1 and ai_choice == 2:
        print("You lose")
    elif choice == 2 and ai_choice == 0:
        print("You lose")
    else:
        print("You win")
