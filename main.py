name = input("Type your name: ")

print("Welcome ", name, "to this adventure!")

answer = input("You are on dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer=="left":
    answer = input("You come to a river, you can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ").lower()
    
    if answer == "walk":
        print("You walked for miles and miles, ran out of water and died of thirst. Game over!")
    elif answer == "swim":
        print("You swam across and met a crocodile. You are eaten by the crocodile. Game over!")
    else:
        print("Not a valid option. You lose!")

elif answer=="right":
    answer = input("You come to a clearing, you can rest or keep walking. Type 'rest' to rest or 'walk' to keep walking: ").lower()
    if answer == "rest":
        print("You rested and regained your strength. You continue your adventure!")
    elif answer == "walk":
        print("You walked for hours and got lost in the woods. Game over!")
    else:
        print("Not a valid option. You lose!")
elif answer == "straight":
    answer = input("You find a treasure chest. Do you want to open it or leave it? Type 'open' to open it or 'leave' to leave it: ").lower()
    
    if answer == "open":
        print("You found gold and jewels! You win!")
    elif answer == "leave":
        print("You left the treasure behind and continued your journey. Game over!")
    else:
        print("Not a valid option. You lose!")
else:
    print("Not a valid option. You lose!")