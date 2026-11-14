"""
    Harley's 3rd Generation Blackjack
"""

from random import *
from time import *

from cardCreation import *    #    Adds all the card values from the file cardCreation.py

print("Thank You For Playing My Blackjack Game\n")
sleep(0.5)

""" - - - - A function to validate user input as a number that takes a question and higher / lower bounds as parameters - - - - """
def integerInputValidation(text,higher,lower):
    while True:
        attempt = input(text)
        if attempt != "":
            try:
                attempt = float(attempt)
            except ValueError:
                print("ERROR : Invalid Data Type\n        Please Enter A Number\n")
                continue
            if attempt % 1 != 0:
                print("ERROR : Invalid Number\n        Please Enter A Whole Number\n")
                continue
            if lower != None and attempt < lower:
                print(f"ERROR : Invalid Range\n        Please Enter A Number Higher Than {lower}\n")
                continue
            if higher != None and attempt > higher:
                print(f"ERROR : Invalid Range\n        Please Enter A Number Lower Than {lower}\n")
                continue
            attempt = int(attempt)
        return attempt

""" - - - - A function to initialise player chips - - - - """
def chipsInitialiser():
    chips = integerInputValidation("How many chips would you like to start with: ", None , 1)
    if chips == "":
        chips = 100
    print(f"⛃⛂ {chips}")
    sleep(0.5)

""" - - - - A function to start / restart the program - - - - """
def start():
    global chips , deck , unShuffledCards , blankDeck
    chips = chipsInitialiser()
    deck = []
    deck = unShuffledCards.copy()
    shuffle(deck)
    blankDeck = createBlankDeck()
    Main()

""" - - - - - Main Program - - - - """
def Main():
    print("\nOriginal Deck:")
    print(*unShuffledCards)
    sleep(0.5)
    print("\nShuffling Deck ...\n")
    sleep(0.5)
    print("New Deck:")
    print(*blankDeck)

start()