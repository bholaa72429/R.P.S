# Component 9 - looping
            # add an game statistics
import random

def h1_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print
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
    error = "Please enter Rock(r), Paper(p) or Scissor(s)"

    while not valid:
        try:
            ans1 = input(question)
            #To remove space from the user input
            answer = ans1.replace(" ","")
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
    rounds_played = 0
    num_won = 0
    num_lose = 0
    num_tie = 0

    while rounds_played < rounds:
        print("Round {} of {}".format(rounds_played+1,rounds))
        guess = ""
        #rounds_played += 1

        choice = wordcheck("Please enter Rock(r), Paper(p) or Scissor(s) ")
        choice = choice.lower()
        token = ["rock", "paper", "scissor"]
        computer_choice = random.choice(token)
        result = ""


        if choice == 'rock':
            if computer_choice == 'rock':
                result = "It's a Tie"
                num_tie += 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"-")
            elif computer_choice == 'paper':
                result = "You Lose"
                num_lose +=1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"~")
            elif computer_choice == 'scissor':
                result = "You Won"
                num_won += 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"#")
            else:
                print("Please enter correct choice.")


        if choice == 'paper':
            if computer_choice == 'paper':
                result = "It's a Tie"
                num_tie += 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"-")
            elif computer_choice == 'scissor':
                result = "You Lose"
                num_lose +=1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"~")
            elif computer_choice == 'rock':
                result= "You Won"
                num_won += 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"#")
            else:
                print("Please enter correct choice.")

        if choice == 'scissor':
            if computer_choice == 'scissor':
                result = "It's a tie"
                num_tie += 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"-")
            elif computer_choice == 'rock':
                result = "You lose"
                num_lose+= 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"~")
            elif computer_choice == 'paper':
                result = "You won"
                num_won+=1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"#")
            else:
                print("Please enter correct choice.")
        rounds_played +=1

        print()
        # Calculate (and then print) game statistics
    print(" End Game Summary ")
    h1_statement("Won: {}  | Lose:{} | Tie: {}".format(num_won,num_lose,num_tie),"*")
    print()
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()
    h1_statement("Thanks For Playing","-")
