# ==========================================
#       Stone Paper Scissors Game 🎮
# ==========================================
# Instructions:
# For enabling cheats write "pro" OR "max" OR "noob" OR "hacker" In end of name input
# For not enabling cheats write any name in input
# Use pip install pyttsx3 (if not) (for no error)
# In user input do not directly press "enter" without giving input(for no error)
# Works in windows
# ==========================================

# Imports
import random as r # built in module
import pyttsx3 as sp # pip install pyttsx3

# Speech Setup
engine = sp.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 for voice 1 and 1 for voice 2

# Functions
def speak(text):
    """Speaks text (using pyttsx3)"""
    engine.say(text)

# Welcome Speech
speak("Welcome to, Stone Paper Sissors Game")
speak("Ye Koi Bacho Wala Game Nahi Haie,")
speak("Pakde Gaye, Toe, Maarae Jaauo Gae")

# Game Name
print("\n\n")
print(("Stone🥔 Paper📄 Sissors✌🏻").center(164))
print("\n\n")

# Score Setup
score = 0
comp_score = 0

# speech
speak("Enter Your name")
engine.runAndWait() # for running (pyttsx3)
engine.runAndWait()

# Name Input
name = str(input('Enter Your name: '))
name = name.upper() # change name to uppercase

# Game Loop
while True:
    # Random computer choice
    comp = int(r.randint(0, 2)) # random(module) feature
    # for activating cheats
    if comp == 0:
        bot = 1
    elif comp == 1:
        bot = 2
    elif comp == 2:
        bot = 0
    # Cheat Codes (cheats)
    if name.endswith("PRO"):
        print(f"The Computer has selected {comp}. Take {bot}") # shows what computer has taken and what you have to take
    if name.endswith("MAX"):
        print(f"The Computer has selected {comp}. Take {bot}") # shows what computer has taken and what you have to take
    if name.endswith("NOOB"):
        print(f"The Computer has selected {bot}. Take {comp}") # shows what computer has taken and what you have to take
        score = score * 2 # doubles the current score
    if name.endswith("HACKER"):
        print(f"The Computer has selected {comp}. Take {bot}") # shows what computer has taken and what you have to take
        score += 100 # gives +100 score instead of +1
    # Player Input
    user = 77
    # while loop for invalid inputs
    while (user != "anything" or int(77)):
        # takes user input
        user = int(input("Stone(0) 👊🏻👊🏻👊🏻 //or// Paper(1) 📄📄📄 //or// Sissors(2) ✌🏻✌🏻✌🏻 //or// quit(77) ❌❌❌: "))
        if user == 0 or user == 1 or user == 2:
            break
        print("Wrong Number ❌❌❌") # prints wrong number if wrong input
    # Player Choices (print what user had taken)
    if user == 0:
        print(f"{name}: Stone(0) 👊🏻👊🏻👊🏻")
    elif user == 1:
        print(f"{name}: Paper(1) 📄📄📄")
    elif user == 2:
        print(f"{name}: Sissors(2) ✌🏻✌🏻✌🏻")
    # Computer Choices (print what computer had taken)
    if comp == 0:
        print("Computer: Stone(0) 👊🏻👊🏻👊🏻")
    elif comp == 1:
        print("Computer: Paper(1) 📄📄📄")
    elif comp == 2:
        print("Computer: Sissors(2) ✌🏻✌🏻✌🏻")
    # Result Logic
    # For Draw
    if user == comp:
        print("Its a Draw 🤨🤨🤨🐼🐼🐼")
    # For win
    elif comp == 0 and user == 1:
        print("You Win 🎉🎉🎉✅✅✅✨✨✨")
        score += 1 # score = +1
        comp_score -= 1 # comp score = -1
    elif comp == 1 and user == 2:
        print("You Win 🎉🎉🎉✅✅✅✨✨✨")
        score += 1 # score = +1
        comp_score -= 1 # comp score = -1
    elif comp == 2 and user == 0:
        print("You Win 🎉🎉🎉✅✅✅✨✨✨")
        score += 1 # score = +1
        comp_score -= 1 # comp score = -1
    # For Lose
    elif comp == 1 and user == 0:
        print("You Lose 💀💀💀❌❌❌")
        score -= 1 # score = -1
        comp_score += 1 # comp score = +1
    elif comp == 2 and user == 1:
        print("You Lose 💀💀💀❌❌❌")
        score -= 1 # score = -1
        comp_score += 1 # comp score = +1
    elif comp == 0 and user == 2:
        print("You Lose 💀💀💀❌❌❌")
        score -= 1 # score = -1
        comp_score += 1 # comp score = +1
    # Display Scores
    print(f"{name} Score is {score}")
    print(f"Computer Score is {comp_score}")
