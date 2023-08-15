import random

def get_choices():
    options = ["rock","paper","scissors"] #square brackets, list. SQUARE LIST SQUARE LIST
    player_choice = input("Enter a Choice: rock, paper, or scissors: ")
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice} #curly braces DICTIONARY CURLY DICT CURLY DICT
    return choices

def check_win(player, computer):
    print(f"you chose {player}; the computer chose {computer}!")
    if player==computer:
        return("it's a tie")
    elif (player=="rock" and computer=="scissors") or (player=="scissors" and computer=="paper") or (player=="paper" and computer=="rock"):#remember = is assign == is compare
        return("WINNNAR!!")
    else:
        return "LOSER!"
   #so in the codecamp example, he actually does a bunch of elifs to give individual lines for the various combinations (e.g., "paper covers rock! x Loses"), 
   # but I was curious to see if I could fit it into a single elif 
choices = get_choices()
p_choice= choices["player"]
c_choice= choices["computer"]
result = check_win(choices["player"],choices["computer"])
#ok, in this section, I need to figure out why it appears I'm making calls to a dictionary but with list syntax -- all of this code refers back to the choices dictionary,
#but in each case of pulling up the 2nd item in the ordered pair here, it uses square brackets.
print (result)