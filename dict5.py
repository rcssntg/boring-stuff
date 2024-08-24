# spam = {12345: 'Luggage Combination', 42: 'The Answer'}
# print(spam[42])

# DICTIONARIES VS LISTS

# spam = ['cats', 'dogs', 'moose']
# bacon = ['dogs', 'moose', 'cats']
# print(spam==bacon)

# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# print(eggs == ham)

# spam = {'name': 'Zophie', 'age': 7}
# print(spam['color']) # Expect KeyError


# The keys(), values(), and items() Methods

# spam ={'color': 'red', 'age': 42}

# for v in spam.values():
#     print(v)
    
# for k in spam.keys():
#     print(k)
    
# for i in spam.items():
#     print(i)

# spam = {'color': 'red', 'age': 42}
# # print(spam.keys())
# # print(list(spam.keys()))


# for k, v in spam.items():
#     print(f'Key: {k} Value: {v}')

# Checking Wether a Key or Value Exist in a Dictionary

# spam = {'name': 'Zophie', 'age': 7}
# print('name' in spam.keys())
# print('Zophie' in spam.values())
# print('color'  in spam.keys())
# print('color' not in spam.keys())
# print('color' in spam)

# get() method

# picnicItems = {'apples': 5, 'cups': 2}
# print(f'I am bringing {picnicItems.get('cups', 0)} cups.') # f string format
# print(f'I am bringing {picnicItems.get('egss', 0)} eggs.')


# The setdefault() Method

# spam ={'name': 'Pooka', 'age': 5}
# print(spam.setdefault('color', 'black'))
# print(spam.setdefault('color', 'white'))
# print(spam)


# Nested Dictionaries and Lists

# allGuest = {'Alice': {'apples': 5, 'pretzels': 12},
#             'Bob': {'ham sandwiches': 3, 'apples': 2},
#             'Carol': {'cups': 3, 'apple pies': 1}}

# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought

# print('Number of things being brought:')
# # I will be using f string to shorten the syntax
# print( f' - Apples  {totalBrought(allGuest, 'apples')}')
# print( f' - Cups  {totalBrought(allGuest, 'cups')}')
# print( f' - Cakes  {totalBrought(allGuest, 'cakes')}')
# print( f' - Ham Sandwiches  {totalBrought(allGuest, 'ham sandwiches')}')
# print( f' - Apple Pies  {totalBrought(allGuest, 'apple pies')}')

# chat gpt clean verion
all_guests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}

def total_brought(guests, item):
    return sum(guest.get(item, 0) for guest in guests.values())

print('Number of things being brought:')
items = ['apples', 'cups', 'cakes', 'ham sandwiches', 'apple pies']
for item in items:
    print(f' - {item.title()}: {total_brought(all_guests, item)}')
