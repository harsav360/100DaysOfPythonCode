from art import logo

#Add
def add(val1,val2):
    return val1+val2

#Subtract
def subtract(val1,val2):
    return val1-val2

#Multiply
def multiply(val1,val2):
    return val1*val2

#Divide
def divide(val1,val2):
    return val1/val2

def calculator():
    """Perform basic Arthmetic Operations"""
    print(logo)
    operations = {"+":add,"-":subtract,"*":multiply,"/":divide}

    num1 = float(input("What's is the first number?: "))
    num2 = float(input("What's is the second number?: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from the line above: ")

    function = operations[operation_symbol]
    result = function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")

    action = True
    while action:
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")
        if choice == "y":
            operation_symbol = input("Pick an operation: ")
            number = float(input("What's the next number?: "))
            function = operations[operation_symbol]
            num1 = result
            result = function(num1,number)
            print(f"{num1} {operation_symbol} {number} = {result}")
        else:
            action = False

calculator()
