# Simple Hangman game
# input word that should be guessed or choose random word from list
# choose number of available guesses
# make list from word [A,p,p,l,e]
# make players list [_,_,_,_,_,]
# show guessed letters, updated word, remaining tries
# guess: p, [_,p,p,_,_], remaining tries: 4

import random


wordlist = [
    "Batman",
    "MacBook",
    "Printer",
    "Obduction",
    "Sunflower",
    "Towel",
    "Cube",
    "Panther",
    "Country",
]


def getstartingword():
    choice = input("Do you want to choose a word? ")
    if choice == "yes":
        word = input("Type your word: ")
    else:
        word = random.choice(wordlist)
    return word


def play(word):
    empty = ["_" for letter in word.lower()]
    guessed = False
    tries = 6
    guesses = []

    
    while not guessed and tries > 0:
        print(empty)
        print("Guess all letters or be hanged!")
        print(f"{tries} lives left...")
        guess = input("Your guess: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in guesses:
                print('Already guessed!')
            elif guess not in word.lower():
                print(f'Word does not contain: {guess}')
                guesses.append(guess)
                tries -= 1
                if tries < 1:
                    print("You've been hanged!")
            else:
                print(f'{guess} is in the word')
                guesses.append(guess)
                indices = [i for i, letter in enumerate(word.lower()) if letter == guess]
                for index in indices:
                    empty[index] = guess
                if '_' not in empty:
                    print(f"You're a winner!\nThe word is {word}!")
                    guessed = True
                    break
        else:
            print("Please guess single letters only.")



play(getstartingword())
