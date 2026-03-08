import random

print("Welcome to the Rock Paper Scissor game")
print("Choose your action")
user_action = int(input("0 for Rock, 1 for Paper and 2 for Scissors : "))

comp_actions_list = ["Rock", "Paper", "Scissors"]

comp_action = random.choice(comp_actions_list)

print("Your action is : ")
if(user_action == 0):
    print(comp_actions_list[0])
elif(user_action == 1):
    print(comp_actions_list[1])
elif(user_action == 2):
    print(comp_actions_list[2])
else:
    print("Invalid choice by user.")

print("Computers's action is : ")
print(comp_action)

print("The Result is ")

comp_action_idx = comp_actions_list.index(comp_action)

if(user_action == comp_action_idx) :
    print("Its a tie!")
elif(user_action == 0 and comp_action_idx == 1) or (user_action == 1 and comp_action_idx == 2) or (user_action == 2 and comp_action_idx == 0):
    print("You Lost!")
else :
    print("You Won!")   
    
    
    
