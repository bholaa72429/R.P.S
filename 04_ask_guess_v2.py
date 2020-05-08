# enter valid input
# correctly compare use input with comp
# give feedback as result

import random
choice = input("Please choose rock, paper or scissor ")
choice = choice.lower()

token = ["rock", "paper", "scissor"]

computer_choice = random.choice(token)
result = ""


# comparing user choice with computer
if choice == 'rock':
    if computer_choice == 'rock':
        result = "It's a Tie"
    elif computer_choice == 'paper':
        result = "You Lose"
    elif computer_choice == 'scissor':
        result = "You Won"
    else:
        print("Please enter correct choice.")

# comparing user choice with computer
if choice == 'paper':
    if computer_choice == 'paper':
        result= "It's a Tie"
    elif computer_choice == 'scissor':
        result = "You Lose"
    elif computer_choice == 'rock':
        result = "You Won"
    else:
        print("Please enter correct choice.")
# comparing user choice with computer
if choice == 'scissor':
    if computer_choice == 'scissor':
        result = "It's a tie"
    elif computer_choice == 'rock':
        result = "You lose"
    elif computer_choice == 'paper':
        result = "You won"
    else:
        print("Please enter correct choice.")
print("Computer:",computer_choice, " | User: ", choice, " | Result: ", result)


