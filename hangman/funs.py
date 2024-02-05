import sys
from os import system
from time import sleep
from random import randint

def randomizeWord(words, plat):
    x = randint(0, len(words) - 1)
    global word
    word = list(words[x])
    plat.clear()
    for letter in word:     #creates the platform
        plat.append("_")
    return word
    


def check_letter(guess, plat, used_letters):   
    if guess in word:
        system("clear")

        print("Success")    
        sleep(1)
        system("clear")
        plat[word.index(guess)] = guess

    else:
        system("clear")
        
        used_letters.append(guess)
        print("Failure")
        sleep(1)
        system("clear")
        global chances
        chances -= 1

def check_win(plat, used_letters):    #checks if you guessed the word already
    if "_" not in plat:
        global chances
        chances = 5
        used_letters.clear()
        plat.clear()
            
        for letter in word: #recreates the platform
            plat.append("_")

        system("clear")
        print("You win!")
        sleep(2)
        system("clear")
        

        return 1
    
def check_input(guess, used_letters):     #checks if the input is valid
    if len(guess) != 1:
        system("clear")
        print("Your guess is longer than a letter!")
        sleep(1)
        system("clear")

        return 1

    elif guess in used_letters:       #checks if the guess is already used
        system("clear")
        print(guess + " already used!")
        sleep(1)
        system("clear")

        return 2