# Component 10 - final
# to do ...
# add instructions
import random
#statement generator for the Output of the rounds
def h1_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

#statement generator for the End Game Summary
def h2_statement(statement,statement2, char):
    print()
    print(char*len(statement2),statement2,char*len(statement2))
    print(statement)
    print(char*len(statement))
    print

# Integer checking function below
#checking input from user for No of rounds
def intcheck(question,low,high):
    valid = False
    error = "Whoops! Please enter an integer "
    while not valid:
        try:
            response1 = (input(question))
            #check response is to exit
            if response1 == "xxx":
                return exit()

            response = int((response1))

            if low <= response <= high:
                return response
            else:
                print("Please Enter a Number between 1 and 10")
                print()

        except ValueError:
            print(error)


def wordcheck (question):
    valid = False
    error = "Whoops! Wrong Input."

    while not valid:
        try:
            ans1 = input(question)
            #To remove space from the user input
            answer = ans1.replace(" ","")
            reply = answer.lower()
            #check response is to exit
            if reply == "xxx":
                return exit()
            if reply == "r" or reply=="rock":
                r1 = "rock"
                return r1
            elif reply == "p" or reply=="paper":
                 r2 = "paper"
                 return r2
            elif reply == "s" or reply=="scissor":
                 r3 = "scissor"
                 return r3
            else:
                print(error)
        except ValueError:
            print(error)
# Instructions
h1_statement("---        Rock  /  Paper  /  Scissor - Instruction       ---","-")
print("--> For each game either choose the number of rounds . \n"
        "--> Note that you can only play a maximum of 10 rounds.\n"
      "--> You can quit the game at any point by simply typing 'xxx'.\n"
       "--> When prompted choose Rock / Paper / Scissors\n"
       "--> At the end of each game, you will be provided with a game summary.\n"
       "--> At that point you can either pay again ( press <enter> when prompted)\n"
      "     or quit by pressing any key.\n"
      "-------------------------------------------------------------")



# Main routine
# Loop entire game
con_mode = 0
keep_going = ""
while keep_going == "":
    rounds = intcheck("How many rounds would you like to play ? ", 1, 10)
    rounds_played = 0
    num_won = 0
    num_lose = 0
    num_tie = 0
    con_mode += 1

# Rounds starts
    while rounds_played < rounds:
        # checking and displaying for rounds and continous mode
        if con_mode == 1:
            print()
            print("Round {} of {}".format(rounds_played+1,rounds))
            print()
        else:
            print()
            print(" Continous Mode: Round {} ".format(rounds_played+1))
            print()


        choice = wordcheck("Please enter Rock(r), Paper(p) or Scissor(s) ")

        token = ["rock", "paper", "scissor"]
        computer_choice = random.choice(token)
        result = ""

        # Comparing the user input with random generation
        if choice == 'rock':
            if computer_choice == 'rock':
                result = "It's a Tie"
                num_tie += 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"-")
            elif computer_choice == 'paper':
                result = "You Lose"
                num_lose +=1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"~")
            else:
                result = "You Won"
                num_won += 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"#")



        if choice == 'paper':
            if computer_choice == 'paper':
                result = "It's a Tie"
                num_tie += 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"-")
            elif computer_choice == 'scissor':
                result = "You Lose"
                num_lose +=1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"~")
            else:
                result= "You Won"
                num_won += 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"#")


        if choice == 'scissor':
            if computer_choice == 'scissor':
                result = "It's a tie"
                num_tie += 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"-")
            elif computer_choice == 'rock':
                result = "You lose"
                num_lose+= 1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"~")
            else:
                result = "You won"
                num_won+=1
                h1_statement("User: {} | Computer: {} | Result: {}".format(choice,computer_choice,result),"#")

        rounds_played +=1

        print()

        # Display  game statistics

    h2_statement("   Won: {}     |    Lose: {}    |    Tie: {}   ".format(num_won,num_lose,num_tie),"End Of Summary","/")
    print()
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()

# farewell the user
h1_statement("Thanks For Playing","-")
