# Nombre: Bryner Amparo
# Matricula: 2020-10415

import random
import sys


def main():
    guess_the_number()
    try_again()


def guess_the_number():
    number = (random.randint(0, 100))
    tries = 0
    print("---------------------------------------------\nYou need to guess a number between 0 and "
          "100\n---------------------------------------------")
    while tries < 999999999999999:
        guess = float(int(input("Please enter a number: ")))
        tries = tries + 1
        if guess < number:
            if (number - guess) < 10:
                print("Your guess is hot")
            else:
                print("Your guess is cold")
            print("Your guess is low.")
        elif guess > number:
            if (guess - number) < 10:
                print("Your guess is hot")
            else:
                print("Your guess is cold")
            print("Your guess is high.")
        else:
            break
    print("-------------------------------------------\nGood job! You guessed my number in", tries,
          "tries!\n-------------------------------------------")


def try_again():
    again = "y"
    while again == "y" or again == "Y" or again == "yes" or again == "Yes":
        again = input("Would you like to play again? ")
        if again == "y" or again == "Y" or again == "yes" or again == "Yes":
            return main()
        else:
            return sys.exit(0)


main()
