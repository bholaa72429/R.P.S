import random


def wordcheck (question):
    valid = False
    error = "please enter Rock(r), Paper(p) or Scissor(s)"

    while not valid:
        try:
            answer = input(question)
            reply = answer.lower()
            if reply == "r" or reply=="rock":
                r1 = "Rock"
                return r1
            elif reply == "p" or reply=="paper":
                 r2 = "Paper"
                 return r2
            elif reply == "s" or reply=="scissor":
                 r3 = "Scissor"
                 return r3
            else:
                print(error)
        except ValueError:
            print(error)


choice = wordcheck("Please choose rock, paper or scissor ")
choice = choice.lower()

token = ["rock", "paper", "scissor"]

computer_choice = random.choice(token)
result = ""




if choice == 'rock':
    if computer_choice == 'rock':
        result = "It's a Tie"
    elif computer_choice == 'paper':
        result = "You Lose"
    elif computer_choice == 'scissor':
        result = "You Won"
    else:
        print("Please enter correct choice.")


if choice == 'paper':
    if computer_choice == 'paper':
        result = "It's a Tie"
    elif computer_choice == 'scissor':
        result = "You Lose"
    elif computer_choice == 'rock':
        result= "You Won"
    else:
        print("Please enter correct choice.")

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

# Calculate (and then print) game statistics





