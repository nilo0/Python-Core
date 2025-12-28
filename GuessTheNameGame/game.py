import pandas as pd
import random

all_names = pd.read_csv("./names.csv")["eng"].dropna().astype("str")
guessed_name = list()

first_name = input('Lets play a game! Who can name a name with last letter of the last name Wins!!! Remember not to repeat any name! Confusing Huh? Give me Persian name (finglish please!)').strip().lower()


def find_name(prev_name: str, list_name: list[str], guessed_list: list[str]) -> str | None: 

    if prev_name in guessed_list: 
        print("You lost! this name was guessed before!!!! Boooo")
        return None

    l_last = prev_name[-1]

    candidates = [n for n in list_name if n not in guessed_list and n[0] == l_last]

    if len(candidates) > 0: 
        new_guess = random.choice(candidates).strip().lower()
        guessed_list.append(new_guess)
        return new_guess
    
    else: 
        return None 

name = find_name(first_name, all_names, guessed_name) 
print("My guess is: " + name)

while name:
    name = input('your turn!   ')
    new_name = find_name(name, all_names, guessed_name)
    print("Hmmm! then my guess is "+ new_name)
    name = new_name