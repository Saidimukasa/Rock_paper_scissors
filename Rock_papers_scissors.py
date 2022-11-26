# import the Random Module to Randomise the Choices to be Made
import random

while True:
#     Allowing user to enter choice 
    user_action = input("Enter a choice (rock, paper, scissors): ")
#     Shuffling the Choices from the List
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
#     Getting the Computer suggestion 
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#     Validating the Entries with the computer's
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
#      Asking the User if they want to play againg 
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
