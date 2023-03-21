#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for i in range(nr_letters):
#     password.append(letters[random.randint(0,51)])
# for i in range(nr_numbers):
#     password.append(numbers[random.randint(0,9)])
# for i in range(nr_symbols):
#     password.append(symbols[random.randint(0,8)])
# unique_password = "".join(password)
# print("Your unique password is "+unique_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

limit = nr_letters+nr_numbers+nr_symbols
i = 0
letter_limit = 0
number_limit = 0
symbol_limit = 0

while i < limit:
    choice = random.randint(0,2) #0 -> Letter, 1 -> Symbol, 2 -> Number
    if choice == 0 and letter_limit < nr_letters:
        password.append(letters[random.randint(0,51)])
        i += 1
        letter_limit += 1
    elif choice == 1 and number_limit < nr_numbers:
        password.append(numbers[random.randint(0,9)])
        i += 1
        number_limit += 1
    elif symbol_limit < nr_symbols:
        password.append(symbols[random.randint(0,8)])
        i += 1
        symbol_limit += 1
unique_password = "".join(password)
print("Your unique password is "+unique_password)

#Another way is to use concept of Easy one and then Shuffle the list
#random.shuffle(password_list)
