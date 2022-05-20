import random
import os

clear = lambda: os.system('clear' or  'cls')

def Game():

    print('''\t----{Developed By Vaibhaw mishra}----

\n\nWELCOME TO THE GAME, GUESS THE CORRECT NUMBER

\n\tYou have to guess between 0-50\n\n''')
    
    num = random.randint(0, 50)
    nog = 7
    while(nog > 0):
        print("Number of chances left is:", nog)
        userNum = int(input("\nEnter a number: "))
        if userNum > num:
            print("\nThe number entered is greater than actual number\nTry Again!\n")
            print("-----------------------------------------------\n")
            nog = nog -1
            continue
        elif userNum < num:
            print("\nThe number entered is less than actual number\nTry Again!\n")
            print("-----------------------------------------------\n")
            nog = nog -1
            continue
        else:
            print("\n\n\tCongrats!! You Have Guessed The Number\n\n")
            break
    print("GAME OVER!!\n\n")
    again()

def again():
    x = input("Do You Wish to play again? (Y/n): ")

    if x == 'y':
        clear()
        Game()

    elif x == 'n':
        clear()
        print("\nThank You for playing")

    else:

        again()

Game()
