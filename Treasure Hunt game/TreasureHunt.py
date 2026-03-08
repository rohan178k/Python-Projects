print("Welcome to treasure island! ")
print("Your mission is to find the treasure.")

choice_1 = input("Do you want to go left or right? : ").lower()
if(choice_1 == "right"):
    print("Game Over!")
elif(choice_1 == "left") : 
    choice_2 = input("you are at the lake. Do you want to swim or wait? : ").lower()
    if(choice_2 == "swim") : 
        print("Game Over!")
    elif(choice_2 == "wait") :
        print("There are 3 doors in front of you - Red, Yellow and Blue.")
        choice_3 = input("Which door do you want to choose? : ").lower()
        if(choice_3 == "red" or choice_3 == "blue") :
            print("Game Over!")
        elif (choice_3 == "yellow") :
            print("You found the treasure!!")
        else :
            print("Invalid choice")
    else :
        print("Invalid choice")
else :
    print("Invalid choice")