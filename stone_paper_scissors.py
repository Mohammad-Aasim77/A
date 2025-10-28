# ==========================================
#       Stone Paper Scissors Game 🎮
# ==========================================
# Instructions:
# For enabling cheats write "pro" OR "max" OR "noob" OR "hacker" In end of name input
# For not enabling cheats write any name in input
# ==========================================

# Imports
import random as r # built in module (for random computer input)
import functools as ft # built in module (for fast speed of the game)

# Game Name
print("\n\n")
print(("Stone🥔 Paper📄 Sissors✌🏻").center(164))
print("\n\n")

@ft.lru_cache(maxsize=None) # for increasing speed of same inputs repeated
def main_game():
    # Score Setup
    score = 0
    # Name Input
    name = str(input('Enter Your name: '))
    name = name.upper() # change name to uppercase
    # Game Loop
    while True:
        # Random computer choice
        comp = int(r.randint(0, 2)) # random(module) feature
        # for activating cheats
        if comp == 0: bot = 1
        elif comp == 1: bot = 2
        elif comp == 2: bot = 0
        # Cheat Codes (cheats)
        if name.endswith("PRO") or name.endswith("MAX"): print(f"The Computer has selected {comp}. Take {bot}") # shows what computer has taken and what you have to take
        elif name.endswith("NOOB"):
            print(f"The Computer has selected {bot}. Take {comp}") # shows what computer has taken and what you have to take
            score = score * 2 # doubles the current score
        elif name.endswith("HACKER"):
            print(f"The Computer has selected {comp}. Take {bot}") # shows what computer has taken and what you have to take
            score += 100 # gives +100 score instead of +1
        # Player Input
        # try except with while loop for invalid inputs
        @ft.lru_cache(maxsize=None) # for increasing speed of same inputs repeated
        def user_input():
            user = 99
            while (user != 77):
                try: # takes user input
                    user = int(input("Stone(0) 👊🏻👊🏻👊🏻 //or// Paper(1) 📄📄📄 //or// Sissors(2) ✌🏻✌🏻✌🏻 //or// quit(77) ❌❌❌: "))
                    if user == 0: return 0
                    elif user == 1: return 1
                    elif user == 2: return 2
                    if user == 0 or user == 1 or user == 2: break
                except: print("Invalid Input ❌❌❌") # prints invalid input if wrong input
        user = user_input()
        # Player Choices (print what user had taken)
        if user == 0: print(f"{name}: Stone(0) 👊🏻👊🏻👊🏻")
        elif user == 1: print(f"{name}: Paper(1) 📄📄📄")
        elif user == 2: print(f"{name}: Sissors(2) ✌🏻✌🏻✌🏻")
        # Computer Choices (print what computer had taken)
        if comp == 0: print("Computer: Stone(0) 👊🏻👊🏻👊🏻")
        elif comp == 1: print("Computer: Paper(1) 📄📄📄")
        elif comp == 2: print("Computer: Sissors(2) ✌🏻✌🏻✌🏻")
        # Result Logic
        @ft.lru_cache(maxsize=None) # for increasing speed of same inputs repeated
        def check():
            # For Draw
            if user == comp: print("Its a Draw 🤨🤨🤨🐼🐼🐼")
            # For win
            elif comp == 0 and user == 1:
                print("You Win 🎉🎉🎉✅✅✅✨✨✨")
                return 1 # score = +1
            elif comp == 1 and user == 2:
                print("You Win 🎉🎉🎉✅✅✅✨✨✨")
                return 1 # score = +1
            elif comp == 2 and user == 0:
                print("You Win 🎉🎉🎉✅✅✅✨✨✨")
                return 1 # score = +1
            # For Lose
            elif comp == 1 and user == 0:
                print("You Lose 💀💀💀❌❌❌")
                return -1 # score = -1
            elif comp == 2 and user == 1:
                print("You Lose 💀💀💀❌❌❌")
                return -1 # score = -1
            elif comp == 0 and user == 2:
                print("You Lose 💀💀💀❌❌❌")
                return -1 # score = -1
        score += check()
        # Display Scores
        print(f"{name}: Score is {score}")

main_game()

# For Safety To avoid repetation of imported functions
if __name__ == "__main__":
    ()
