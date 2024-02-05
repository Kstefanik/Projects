import sys
from os import system
from time import sleep
from random import randint
from funs import *


words = ["ex1", "ex2", "ex3"]   #put in words to quess


chances = 5
used_letters = []
plat = []


########################### Main ##################################
while True:
    randomizeWord(words, plat)


    print("1.Play")
    print("2.Exit")
    menuChoice = int(input("Enter a number: "))
    
    if menuChoice == 1:
        system("clear")
        print("Game start")
        sleep(1)
        system("clear")

    elif menuChoice == 2:
            sys.exit()

    else:
        print("Invalid input!")
        sleep(1)
        system("clear")
        continue

    while True:
        print(plat)
        if chances == 0:        #checks whether you ran out of chances
            chances = 5
            used_letters.clear()
            plat.clear()
            
            for letter in word: #recreates the platform
                plat.append("_")

            system("clear")
            print("You lose!")
            sleep(2)
            system("clear")
            break

        print(f"Chances: {chances}")
        print(f"Used letters: {used_letters}")

        guess = input("Enter a letter: ")

        if check_input(guess, used_letters) == 1:     #checks input
            continue
        elif check_input(guess, used_letters) == 2:
            continue

        check_letter(guess, plat, used_letters)
        if check_win(plat,used_letters) == 1:
            break
        


