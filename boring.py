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


def sophia_bday():
    print('Happy birthday!')
    
print('What is your name?') 
name = input() 
print('How old are you?')
age = input()

print(f'Hello {name} you are {age} years old now, that is nice!')
print(sophia_bday)