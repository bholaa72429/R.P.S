# **user input**
# ask the number of rounds
# provide a round counter
# ask their guesses

# Integer checking function below
# Number checking function goes here
def intcheck(question, low=None, high=None):

    # error messages
    if low is not None and high is not None:
            error = "Please enter an integer between {} and {}" \
            "(inclusive)".format(low, high)

    elif low is not None and high is None:
        error = "please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "please enter an integer that is less than or "\
                "equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))

            # check response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # checks response is not too high
            if high is not None and response > high:
                 print(error)
                 continue




