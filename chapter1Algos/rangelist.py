"""
Demonstrate how to use pythons list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256]
"""

#l = [x*x for x in ]

#write out a for loop

l = []                  #empty list
for i in range(9):      #creates 9 numbers in a list
    l.append(2**i)      #base 2 will be raised to the power 0,1,2,3,4,...to 8 because n-1
print(l)                # = [1, 2, 4, 8, 16, 32, 64, 128, 256]

#-------------------------------List Comprehension----------------------------------

lx = [2**i for i in range(0, 9)]

print(lx)


print([pow(2, k) for k in range(0, 9, +1)])
