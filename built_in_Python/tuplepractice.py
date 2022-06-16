mytup = ('CJ', 27, 'Tampa', 'Florida') #tuple
mytup1 = ('dom',) # a comma is needed for even one element of a tuple
mytup2 = 'ghost', 'german shepard', 'white' #still is a tuple without the ()

print(mytup1)
print(mytup)
print(mytup2)



print(mytup.count("CJ")) #returns 1
print(mytup.count('cj')) #returns 0

print(mytup.index('Tampa')) #returns 2


mylist = list(mytup2) #list funtion turns tuple into list
print(mylist)

mytuple = tuple(mylist) #turns list into a tuple
print(mytuple)

a = (1, 2, 3, 4,5,5,6,7,8,9)
b = a[::] #print entire tuple
print(b)
b = a[::-1] #reverses entire tuple
print(b)

x, *b, c = a #indexes in the tuple (10 elements, x = 1, *b = 2 through 8, c = 9)
print(x)
print(*b)
print(c)


import sys

z = [1,2, 3,4,5,6,7,8]
y = (1,2, 3,4,5,6,7,8)

print(sys.getsizeof(z)) #gets bytes for list
print(sys.getsizeof(y)) #gets bytes for tuple, tuple is smaller 120 to 104

import timeit

print(timeit.timeit(stmt = '[0,1,2,3,4,5]' , number = 1000000))#0.053095886
print(timeit.timeit(stmt = '(0,1,2,3,4,5)', number = 1000000)) #0.007138865000000008 tuples are faster and take less memory 
