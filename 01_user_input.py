# **user input**
# ask the number of rounds
# provide a round counter
# ask their guesses

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

rounds = intcheck("How many rounds would you like to play with ? ", 1, 10)


rounds_played = 0
while rounds_played < rounds:

    print("Round {}".format(rounds_played+1))
    guess = input("Enter Rock(r) / Paper(p) / Scissors(s)")
    rounds_played += 1

