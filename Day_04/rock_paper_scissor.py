import random
import my_module

print("Welcome to Rock - Paper - Scissors")
# print(my_module.rock)
# print(my_module.paper)
# print(my_module.scissors)
mylist = [my_module.rock, my_module.paper, my_module.scissors]


answer = int(input("Make Your Choice -> Rock(0) - Paper(1) - Scissors(2) : "))
print("Your Choice :")
if (answer >= 3):
     print("Invalid number O_O")
else:  
    print(mylist[answer])


    compChoice = random.randint(0,2)
    print("Computer choice :")
    print(mylist[compChoice])   

    if ((compChoice == 0 and answer == 2) or (compChoice == 1 and answer == 0) or (compChoice == 2 and answer == 1)) :
        print("Computer Wins !!!")
    elif ((compChoice == 2 and answer == 0) or (compChoice == 0 and answer == 1) or (compChoice == 1 and answer == 2)) :
        print("You Wins !!!")
    elif (compChoice == answer):
        print("Draw !!!")
    else : 
        print("Invalid number O_O")

#Another approach : 

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")





