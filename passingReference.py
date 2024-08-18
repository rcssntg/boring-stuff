# def eggs(someParameter):
#     someParameter.append('Hello')

# spam = [1, 2, 3]
# eggs(spam)
# print(spam)


# copy Module's copy() and deepcopy() functions
import copy

spam =['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42

print(spam)
print(cheese)