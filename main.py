MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water : {water}ml")
    print(f"Milk : {milk}ml")
    print(f"Coffee : {coffee}gm")
    print(f"Money : $ {profit}")





def check_resource(choice):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    if choice == "espresso":
        if water >= MENU["espresso"]["ingredients"]["water"] and coffee >= MENU["espresso"]["ingredients"]["coffee"]:
            return True
        else:
            return False
    elif choice == "latte":
        if water >= MENU["latte"]["ingredients"]["water"] and coffee >= MENU["latte"]["ingredients"][
            "coffee"] and milk >= MENU["latte"]["ingredients"]["milk"]:
            return True
        else:
            return False
    else:
        if water >= MENU["cappuccino"]["ingredients"]["water"] and coffee >= MENU["cappuccino"]["ingredients"][
            "coffee"] and milk >= MENU["cappuccino"]["ingredients"]["milk"]:
            return True
        else:
            return False


def process_coins(choice, total):
    moneyNeed = MENU[choice]["cost"]
    if total >= moneyNeed:
        extra = round(total - moneyNeed, 2)
        global profit
        profit += moneyNeed
        if extra > 0:
            print(f"Here is ${extra} in change.")
        return True
    else:
        return False


def make_coffee(choice):
    if check_resource(choice):
        print("Please insert the coins.")
        quarters = int(input("How many quarters?:"))
        dimes = int(input("How many dimes?:"))
        nickels = int(input("How many nickels?:"))
        pennies = int(input("How many pennies?:"))
        total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
        if process_coins(choice, total):
            print(f"Here is your {choice} ☕. Enjoy!")
        else:
            print("Sorry, Money is not Sufficient ! Refunded")
    else:
        print("Not Enough Resources")


machine = True

while machine:
    choice = input("What would you like ? (espresso/latte/cappuccino) : ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print_report()
    else:
        make_coffee(choice)
