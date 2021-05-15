#----------LIBRARIES-------------------
import random, time
#--------------------------------------
moves = 6
guess = ''
#----our words-------------------------


#--------------------------------------
def introduction():
    time.sleep(1)
    starting_point()
    print('')
    time.sleep(1)
    print("Welcome in hangman!")
    time.sleep(1)
    print('')
    

#-----------choices----------------------------------------------
def choice():
    choice = input("do you wanna play?\ny \ n \nyour choice: ")
    if choice == 'y':
        print("Great!")
        time.sleep(1)
        guessing()
    elif choice == 'n':
        print("so bye!")
        exit()
    else:
        print('please to choose between y or n. "y = yes, n = no"')
        time.sleep(1)
        choice1()

def choice1():
    print("")
    choice = input("do you wanna play?\ny \ n \nyour choice: ")
    if choice == 'y' or choice == 'Y':
        print("Great")
        guessing()
    elif choice == 'n' or choice == 'N':
        print("so bye!")
        exit()
    else:
        print('please to choose between y or n. "y = yes, n = no"')
        time.sleep(1)

def play_again():
    choice = input("do you wanna play again?\ny \ n \nyour choice: ")
    if choice == 'y':
        print("so.. play again!")
        time.sleep(1)
        guessing()
    elif choice == 'n':
        print("so bye!")
        exit()
    else:
        print('please to choose between y or n. "y = yes, n = no"')
        time.sleep(1)
        choice1()

#----------------------------------------------------------------------

def guessing():
    words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
    secret = random.choice(words)
    guesses = ''
    moves = 6
    while moves > 0: 
        fails = 0 
        for char in secret: 
            if char in guesses:
                print(char)
            else:
                print("_")
                fails += 1
        if fails == 0:
            print("You win!")
            time.sleep(1)
            print("The secret word is: ", word)
            time.sleep(1)
            play_again()
            
        
        guess = input("guess a character: ")

        guesses += guess

        if guess not in secret:
            moves -= 1
            print("Wrong!\nyou have", + moves, 'more guesses')
            if moves == 5:
                step_one()
            elif moves == 4:
                step_two()
            elif moves == 3:
                step_three()
            elif moves == 2:
                step_four()
            elif moves == 1:
                step_five()
            else:
                step_six()     
                time.sleep(1)
                play_again()
            
#-----------------------------------------------------------------------
def starting_point():
    print("----------------------------------------------------------------")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                       ____                                   |")
    print("|                      |   |                                   |")
    print("|                          |                                   |")
    print("|                          |                                   |")
    print("|                          |                                   |")
    print("|                          |                                   |")
    print("|                         /|\                                  |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("----------------------------------------------------------------")


def step_one():
    print("----------------------------------------------------------------")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                       ____                                   |")
    print("|                      |   |                                   |")
    print("|                      O   |                                   |")
    print("|                          |                                   |")
    print("|                          |                                   |")
    print("|                          |                                   |")
    print("|                         /|\                                  |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("----------------------------------------------------------------")

def step_two():
    print("----------------------------------------------------------------")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                       ____                                   |")
    print("|                      |   |                                   |")
    print("|                      O   |                                   |")
    print("|                      |   |                                   |")
    print("|                          |                                   |")
    print("|                          |                                   |")
    print("|                         /|\                                  |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("----------------------------------------------------------------")

def step_three():
    print("----------------------------------------------------------------")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                       ____                                   |")
    print("|                      |   |                                   |")
    print("|                      O   |                                   |")
    print("|                     \|   |                                   |")
    print("|                          |                                   |")
    print("|                          |                                   |")
    print("|                         /|\                                  |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("----------------------------------------------------------------")

def step_four():
    print("----------------------------------------------------------------")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                       ____                                   |")
    print("|                      |   |                                   |")
    print("|                      O   |                                   |")
    print("|                     \|/  |                                   |")
    print("|                          |                                   |")
    print("|                          |                                   |")
    print("|                         /|\                                  |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("----------------------------------------------------------------")

def step_five():
    print("----------------------------------------------------------------")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                       ____                                   |")
    print("|                      |   |                                   |")
    print("|                      O   |                                   |")
    print("|                     \|/  |                                   |")
    print("|                      |   |                                   |")
    print("|                          |                                   |")
    print("|                         /|\                                  |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("----------------------------------------------------------------")

def step_five():
    print("----------------------------------------------------------------")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                       ____                                   |")
    print("|                      |   |                                   |")
    print("|                      O   |                                   |")
    print("|                     \|/  |                                   |")
    print("|                      |   |                                   |")
    print("|                     /    |                                   |")
    print("|                         /|\                                  |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("----------------------------------------------------------------")
    
def step_six():
    print("----------------------------------------------------------------")
    print("|                                                              |")
    print("|                                                              |")
    print("|                                                              |")
    print("|                       ____                                   |")
    print("|                      |   |                                   |")
    print("|                      O   |                                   |")
    print("|                     \|/  |                                   |")
    print("|                      |   |                                   |")
    print("|                     / \  |                                   |")
    print("|                         /|\                                  |")
    print("|                                                              |")
    print("|                 YOU LOST THE GAME                            |")
    print("|                                                              |")
    print("|                                                              |")
    print("----------------------------------------------------------------")

introduction()
choice()
