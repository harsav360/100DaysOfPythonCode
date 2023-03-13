print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direc = input("Left or Right : ")
if direc != "Left":
    print("Fall into hole. Game Over")
else:
    choice = input("Swim or Wait : ")
    if choice != "Wait":
        print("Attacked by trout. Game Over")
    else:
        door = input("Red,Blue,Yellow : ")
        if door == "Yellow":
            print("You win!")
        elif door == "Red":
            print("Burned by fire.Game Over")
        elif door == "Blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over")
