# combine all the pre-vision together
import random
# int-check function
def intcheck(question,low,high):
    valid = False
    error = "Whoops! Please enter an integer "
    while not valid:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print("Please Enter a Number between 1 and 10")
                print()

        except ValueError:
            print(error)

# word check function
def wordcheck(question):
    valid = False
    error = "please enter Rock(r), Paper(p) or Scissor(s)"

    while not valid:
        try:
            answer = input(question)
            reply = answer.lower()
            if reply == "r" or reply == "rock":
                r1 = "rock"
                return r1
            elif reply == "p" or reply == "paper":
                 r2 = "paper"
                 return r2
            elif reply == "s" or reply == "scissor":
                 r3 = "scissor"
                 return r3
            else:
                print(error)
        except ValueError:
            print(error)

#Main Routine
rounds = intcheck("How many rounds would you like to play with ? ", 1, 10)
for x in range(rounds):
    choice = wordcheck("Please choose rock, paper or scissor ")
    token = ["rock", "paper", "scissor"]
    computer_choice = random.choice(token)
    result=""


    if choice == "rock":
        if computer_choice == "rock":
            result = "It's a Tie"
            print("Computer:",computer_choice," | User: ",choice," | Result: ",result)
        elif computer_choice == "paper":
            result = "You Lose"
            print("Computer:",computer_choice, " | User: ", choice, " | Result: ", result)
        else:
            result = "You Won"
            print("Computer:",computer_choice, " | User: ", choice, " | Result: ", result)


    if choice == "paper":
        if computer_choice == "paper":
            result = "It's a Tie"
            print("Computer:",computer_choice, " | User: ", choice, " | Result: ", result)
        elif computer_choice == "scissor":
            result = "You Lose"
            print("Computer:",computer_choice, " | User: ", choice, " | Result: ", result)
        else:
            result = "You Won"
            print("Computer:",computer_choice, " | User: ", choice, " | Result: ", result)


    if choice == "scissor":
        if computer_choice == "scissor":
            result = "It's a tie"
            print("Computer:",computer_choice, " | User: ", choice, " | Result: ", result)
        elif computer_choice == "rock":
            result = "You lose"
            print("Computer:",computer_choice, " | User: ", choice, " | Result: ", result)
        else:
            result = "You won"
            print("Computer:",computer_choice, " | User: ", choice, " | Result: ", result)









