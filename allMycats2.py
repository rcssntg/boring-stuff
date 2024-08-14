catNames = []
while True:
    print(f'Enter the name of cat {str(len(catNames) + 1)} (Or enter nothing to stop.):') # I used f string here
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(f' {name}') # I used f string again here
    