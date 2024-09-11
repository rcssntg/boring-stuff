# Matching Zero or More with the Star

import re

# batRegex = re.compile(r'Bat(wo)*man')

# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())

# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())

# mo3 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo3.group())



# Matching One or More with Plus

# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('The Adventures of Batwoman')
# print(mo1.group())

# mo2 =batRegex.search('The Adventures of Batwowowowoman')
# print(mo2.group())


# mo3 = batRegex.search('The Adventures of Batman')
# print(mo3 == None)




# Matching Specifi Repetition with Curly Brackets

# haRegex = re.compile(r'(Ha){3}')
# mo1 = haRegex.search('HaHaHa')
# print(mo1.group())

# mo2 = haRegex.search('Ha')
# print(mo2 == None)


# Greedy and Nongreedy matching

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())


nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHaHa')
print(mo2.group())