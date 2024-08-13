
def collatz(number):
        if number % 2 == 0:
            print(number // 2)
            return number
        else:
            print( 3 * number + 1)
            return number

 
    
print('Please enter a random number.')
try:
    number = int(input())
    collatz(number)

except:
    print('Oops! You must enter an integer!')
    
