# This is a guess the number game.

import random

# Greet and ask the players name
print('Welcome to guess my number game!')
print('Before we begin. Please enter your name: ')
name = input() # Player's name

print(f'Okay {name} let us play the game!')
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')


# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!
    
# NOTE: I use the " f string methode to concatenate the string"
if guess == secretNumber:
    print(f'Good job {name}! You guessed my number in {guessesTaken} guesses!')
else:
    print(f'Nope. The number I was thinking of was {secretNumber}.')

