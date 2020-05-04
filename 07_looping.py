import random
# Integer checking function below
def intcheck(question,low=1,high=10):
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
keep_going = ""
while keep_going == "":
    rounds = intcheck("How many rounds would you like to play with ? ", 1, 10)
    round_played=0
    while round_played < rounds:

        choice = wordcheck("please enter Rock(r), Paper(p) or Scissor(s) ")
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
        round_played +=1
        print("Computer:",computer_choice, " | User: ", choice, " | Result: ", result)
        print()
    print()
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()
# Calculate (and then print) game statistics
