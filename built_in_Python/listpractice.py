"""
some list problems and practice - built in fucntions practice
"""

color_list = ['red', 'blue', 'yellow', 'black', 'pink', 'green']
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unsorted_list = [84, 2, 9, 0, 1, 99, 99, 12, 100]


print(color_list)
print(number_list)
print(unsorted_list)

for x in range(len(color_list)):
    print(x, color_list[x])

sorted_list = sorted(unsorted_list) #not permanent
for index, item in enumerate(sorted_list):
    print(index, item)

print(unsorted_list)

unsorted_list.sort()    #permanent
print(unsorted_list)

print(unsorted_list[5:]) #prints items past 4th index counting from 0 (9 numbers in total) n-1
unsorted_list.insert(1, -1)
print(unsorted_list) #list is now unsorted until we permantly sort it
print(sorted(unsorted_list)) #[-1, 0, 1, 2, 9, 12, 84, 99, 99, 100] not permanent
color_list.sort()
print(color_list)
color_list.append('orange')
print(color_list)
popped_color = color_list.pop()
print(popped_color)
print(color_list)
color_list.insert(-2, 'white')
print(color_list)
print(color_list[-1:])
color_list.insert(-1, 'purple') #inserted into the -2 index not negative 1
color_list.append('beige') #insert into the last spot
print(sorted(color_list))

print(color_list)
color_list.sort()
print(color_list)
color_list.remove('beige')
print(color_list)
color_list.reverse()
print(color_list)

new_list = [9] * 5 # makes list with 5 number 9's
print(new_list)
new_list.clear() #clears entire list of its contents
print(new_list)

ex1 = [1] *3
ex2 = [2] *3
ex3 = ex1 + ex2 #concatinate two lists
print(ex3)

ex4 = ex3[3:] #new list allows us to print just the ex2 list
print(ex4)

ex5 = ex3[::-1] #copys and reverse list
print(ex5)
ex5_1 = ex3[::]
print(ex5_1)

print(ex3)
ex3_1 = ex3 # this puts both ex3 and ex_3 in the same place in memory BAD use copy() or [::]
ex3_1.append(0)
print(ex3_1)
print(ex3)

#for example copy method first

ex3_2 = ex3.copy()
print(ex3_2)
ex3_2.append(-1)
print(ex3_2)
print(ex3)


#next [::] method

ex3_3 = ex3_2[::]
ex3_3.append(-2)
print(ex3_3)
print(ex3_2)


#list comprehension
listy = [x for x in unsorted_list]
print(listy)

#cretate new list

new_list = [x*2 for x in range(10)]
print(new_list)
