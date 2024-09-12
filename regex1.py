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

# greedyHaRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyHaRegex.search('HaHaHaHaHa')
# print(mo1.group())


# nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nongreedyHaRegex.search('HaHaHaHaHaHa')
# print(mo2.group())


# The findall() Method

# search() method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 412-555-9999 Work: 212-555-0000')
print(mo.group())

# findall() method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))