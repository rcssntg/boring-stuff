import time   

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'mana potion': 12, 'life potion': 3}




def displayInventory(inventory):
    print('Inventory:')
    time.sleep(1)
    for item, quantity in inventory.items():
        print(f'{quantity} {item.title()}')
        time.sleep(.5)
        
def addItem(inventory):
    # Add new item via user input
    newItem = input('Enter the name of the item to add: ').lower()
    count = int(input('Enter the quantity of the item: '))

    # Add the new item to the inventory, or update the quantity if it is already exists
    if newItem in inventory:
        inventory[newItem] += count
    else:
        inventory[newItem] = count
        
    print(f'Added {count} {newItem.title()} to the inventory.')
    time.sleep(.5)
 

displayInventory(stuff)
addItem(stuff)
displayInventory(stuff)