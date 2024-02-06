import sys
from os import system
from time import sleep
from random import randint

words = ["example1", "example2", "example3"]

chances = 5
used_letters = []
plat = []

def randomizeWord():
    x = randint(0, len(words) - 1)
    global word
    word = list(words[x])
    plat.clear()
    for letter in word:     #creates the platform
        plat.append("_")

def find_all_occurrences(word, guess):
    return [index for index, value in enumerate(word) if value == guess]


def check_letter(guess):   
    if guess in word:
        system("clear")

        print("Success")    
        sleep(1)
        system("clear")
        
        occurrences = find_all_occurrences(word, guess)
        
        for occurence in occurrences:
            plat[occurence] = guess
        used_letters.append(guess)
        

    else:
        system("clear")
        
        used_letters.append(guess)
        print("Failure")
        sleep(1)
        system("clear")
        global chances
        chances -= 1



def check_win(plat):    #checks if you guessed the word already
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
        

def check_input(guess):     #checks if the input is valid
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

########################### Main ##################################
while True:
    randomizeWord()

    print(word)

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

        if check_input(guess) == 1:     #checks input
            continue
        elif check_input(guess) == 2:
            continue

        check_letter(guess)
        if check_win(plat) == 1:
            break
        


