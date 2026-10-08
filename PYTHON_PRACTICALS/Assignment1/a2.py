# write a program to guess a number. (Use random())
import random

secret = random.randint(1, 100)
guess = 0
while guess != secret:
    guess = int(input("Guess a number (1-10): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print("You got it!")