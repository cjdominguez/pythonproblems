"""
some practice with for loops, range(len function), & enumarate
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f']

for letter in letters:
    print(letter)

print('\n')

for index in range(len(letters)):
    print("letters", index, " = ", letters[index]) #prints index along with string

print('\n')

for index in range(len(letters)):
    print(index)                                    #prints index only

print('\n')

for index, item in enumerate(letters):              #a more effecient way of getting both the index and item in a list
    print(index, '=',  item)

print('\n')

enum_obj = enumerate(letters)                       #returns iterbale object in the form of a tuple (index, item)
print(next(enum_obj))                               #'next' gets next item in list
print(next(enum_obj))
