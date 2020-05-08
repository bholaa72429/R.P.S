# create word check  function to check users guess
def wordcheck (question):
    valid = False
    error = "please enter Rock(r), Paper(p) or Scissor(s)"

# check lowercase and first letter is valid
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

response = wordcheck("Please choose rock, paper or scissor")

print("Done")




