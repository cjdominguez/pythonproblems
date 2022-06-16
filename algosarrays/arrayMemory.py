x = 5                                                             #is the first object created has a specific refrence address
print(id(x), "new reference address & new object at x = 5")        #refrence address shown here
y = 5               # refrence address same as x above
print(id(y), "refrence is equal to above varianle x = 5 because both y and x = 5 ")        #refrence address shown here

x = 5 + 1           #new frame x is now a differnt object with a differnet refrence address
y = x               #new frame y is now a differnt object with a differnet refrence address

print(id(x), "x = 5 +1 creates new object and refrence from above the previous value of x = 5")
print(id(y), "y = x has same refrence address as x = 6" )

newY = y + 1
print(id(newY), "newY = y + 1 creates new address and object where y = 7 ")

newyy = 6
print(id(newyy), "newyy = 6 taking the previous copying the same refrence number x = 5 and y = x")

plus = y + x
print(id(plus),plus, ", plus = y + x creates new refrence address where plus = 12 becausee 6 + 6 but it got those numbers from the previous placement of x and y")

x = 1
print(id(x), "new address x = 1")

a = None
z = a
print(id(a), "always has a shorter memeory  address because a = none I suppose that number is specific in memory")
print(id(z), "same as refercne address above because  z = a ")
