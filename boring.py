# Automate Boring Stuff with Python

# Python Shell

# Data Types

# Variables

# First Program

# This program says hello and asks for my name.

# print('Hello world!')
# print('What is your name?')    # ask for their name
# myName = input()

# print('It is good to meet you, ' + myName)
# print('The lenght of your name is:')
# print(len(myName))

# print('What is your age?')    # ask for their age
# myAge = int(input())
# # print('You will be ' + str(int(myAge) + 1) + ' in a year.')  
# print('You will be ' + str(myAge + 1) + ' in a year.')  # I put the int() to the input

# i am trying to push using git bash


# Chapter 2 FLOW CONTROL

# print('Is raining? y or n')

# answer = input()

# if answer == 'y':
#     print('Have umbrella? y or n')
#     umbrella = input()
# elif umbrella == 'y':
#         print('Go outside')
# else:
#     print('wait a while')



# name = input('What is your name? ')
# if name == 'Mary':
#     print('Hello Mary')  
 
# password = input('What is your password? ')    
# if password == 'swordfish':
#     print('Access granted.')
# else:
#     print('Wrong password')

# if name == 'Alice':
#     print('Hi Alice')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire')
# elif age > 100:
#     print('You are not Alice, grannie.')

# spam = 0

# if spam < 5:
#     print('Hello world.')
#     spam = spam + 1
    
    
# spam = 0

# while spam < 5:
#     print('Hello world.')
#     spam = spam + 1

# Annoying LOOP (Your name)

# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')

#  BREAK
# while True:
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break
# print('Thank you!')

# while True:
#     print('Hello World.')
    # CTRL-C to STOP
    
# CONTINUE

# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted')


# Truthy and Falsey
# name = ''

# while not name:
#     print('Enter your name:')
#     name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:
#     print('Be sure to have enough room for all your guests.')
# print('Done!')



# for Loops

# print('My name is')
# for i in range(10): 
#     print('Jimmy Five Times (' + str(i) + ')')
#     # break
#     # continue


# Gauss
# total = 0
# for num in range(101):
#     total = total + num
# print(f'The total is {total}')

# Equivalent Loop
# print('My name is')
# i = 0
# while i < 5:
#     print('Jimmy Five Times (' + str(i) + ')')
#     i = i + 1
    
    
# for i in range(1, 101):
#     print(i)
# print('How much is your money?')
# money = int(input())

# footlong = 56
# chizburger = 50

# total = chizburger * 2 + footlong
# change = money - total
# print(f'the total amount is {total} and the change is {change}')

# for i in range(0, 10, 3):
#     print(i)
# for i in range(5, -1, -1):
#     print(i)


# def sophia_bday():
#     print('Happy birthday!')
    
# print('What is your name?') 
# name = input() 
# print('How old are you?')
# age = input()

# print(f'Hello {name} you are {age} years old now, that is nice!')
# sophia_bday()




# IMPORTING MODULES

# import random

# for i in range(5):
#     print(random.randint(1, 11))

# import random, sys, os, math

# import sys
# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print(f'You typed {response}.')
    
    
    
# print('What is the value of spam?')
# spam = int(input())

# if spam == 1:
#     print('Hello')
# elif spam == 2:
#     print('Howdy')
# else:
#     print('Greetings')
# print('For Loops Version')
# for i in range(1, 11):
#     print(i)
    

# print('While Loops Version')
# i = 1
# while i < 11:
#     print(i)
#     i = i + 1



# FUNCTIONS


# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')
    
    
# hello()ronel

# hello()
# hello()

# def hello(name):
#     print(f'Hello {name}, how are you?')
    
    
# print('What is your name?')
# name = input()

# hello(name)
# print(name)

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(r, fortune)

print(getAnswer(random.randint(1, 9)))