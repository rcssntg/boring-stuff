birthdays = {'alice': 'Apr 1', 'bob': 'Dec 12', 'carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quite)')
    name = input().lower()
    if name == '':
        break
    
    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name.capitalize()}')
    else:
        print(f'I do not have birthday information for {name.capitalize()}')
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')