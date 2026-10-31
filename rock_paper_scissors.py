import random


while True :
    user_action = input("Enter any choice you want(rock,paper,scissors):")
    possible_actions = ["rock","paper","scissors"]

    computer_action = random.choice(possible_actions)
    print("Your action = ",user_action)
    print("Computer action = ",computer_action)
    if user_action == computer_action :
        print("It's a tie")
    elif user_action == "rock":
        if computer_action == "scissor" :
            print("You win!")
        else :
            print("You lose !")
    elif user_action == "paper":
            if computer_action == "rock" :
                print("You win!")
            else :
                print("You lose !")
    elif user_action == "scissor":
            if computer_action == "paper" :
                print("You win!")
            else :
                print("You lose !")
    play_again = input("Play again ?")
    if play_again != "y":
         break
    

            
    