# 0 -> Rock, 1 -> Paper, 2 -> Scissors
#Rules -> Rock beats Scissor, Scissor beats paper and paper beats rock(by Covering it)
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
you = int(input("Choose any number between 0 and 2 -> "))
computer = random.randint(0,2)
if you == computer:
    print("Draw")
elif you == 0:
    if computer == 1:
        print("You Lose")
    else:
        print("You Won")
elif you == 1:
    if computer == 2:
        print("You Lose")
    else:
        print("You Won")
else:
    if computer == 0:
        print("You Lose")
    else:
        print("You Won")
    

