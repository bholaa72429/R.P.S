# HL component 8 - Statement Generator

def h1_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

# Main routine
won = h1_statement("^^ You have won this round.^^", "^")
print()
lose = h1_statement("vv You have lost this round: 2 vv", "v")
print()
tie = h1_statement("** its a tie ***", "*")
print()
start_round = h1_statement("### Round 1 of 3 ###", "#")
