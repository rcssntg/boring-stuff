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

spam ={'name': 'Pooka', 'age': 5}
print(spam.setdefault('color', 'black'))
print(spam.setdefault('color', 'white'))
print(spam)