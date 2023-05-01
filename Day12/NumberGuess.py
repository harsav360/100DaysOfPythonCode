from random import randint
from art import logo
print(logo)
number = randint(1,100) #Generating an random number

def Hard_guess():
    lives = 5
    while lives:
        check = int(input("Guess any number between 1 to 100 : "))
        if check == number:
            print(f"You guess it right in {10-lives+1} times and the number is {number} ")
            return
        elif check > number:
            print(f"{check} is too high")
        else:
            print(f"{check} is too low")
        lives -= 1
        print(f"You have {lives} attempts left")
        if lives == 0:
            print("You loose the game, TATA BYE BYE")
            return



def Easy_guess():
    lives = 10
    while lives:
        check = int(input("Guess any number between 1 to 100 : "))
        if check == number:
            print(f"You guess it right in {10-lives+1} times and the number is {number} ")
            return
        elif check > number:
            print(f"{check} is too high")
        else:
            print(f"{check} is too low")
        lives -= 1
        print(f"You have {lives} attempts left")
        if lives == 0:
            print("You loose the game, TATA BYE BYE")
            return
level = input("Choose your difficulty level, Hard or Easy : ")
if level == "Hard":
    Hard_guess()
else:
    Easy_guess()



