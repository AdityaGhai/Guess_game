# This is guess game
import random

secret_number = random.randint(1,20)  #secret number assign here

print("\nThis is a guessing game. You have to choose which number I am thinking, Don't worry I won't lie:) .\n")

for guessesTaken in range(1,7):  #This will limit the number of guessing
    print("Take a guess. \nHint: It is less than 20 and more than 1. ")
    guess = int(input())

    if guess-secret_number>=10:
        print("Too high guess again.")
    elif guess-secret_number>=5:
        print("Your guess is high.")
    elif guess-secret_number>=1:
        print("Little bit high, You are close guess again.")
    elif secret_number-guess >= 10:
        print("Too low guess again.")
    elif secret_number-guess>=5:
        print("Your guess is low.")
    elif secret_number-guess>=1:
        print("Little bit low, You are close guess again.")
    else:
        break  #This is for right guess. It will terminate the for loop.


if guess== secret_number:
    print("Awesome you got it right in " + str(guessesTaken) + " guesses! Cheers:) ")

else:
    print("Bad luck , The number I was thinking of was "+ str(secret_number))
