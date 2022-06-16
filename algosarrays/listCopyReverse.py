
l = [1,2,3,4]
print(l)


l[:] = l[::-1]
print(l)


#only reverses the list in place

t = ['a','b','c','d']
print(t)

t.reverse()
print(t)

#reverses list and leaves the original list intact no copies are made and we are simply walking the indices backwards.
arr = [9,8,7,6,5]
print(arr)
for i in range(1,len(arr)+1):
    print(arr[-i])
print(arr)

#creates
arr1 = [1,2,3,4,5]
for i in arr1[::-1]:
    print(i)
print(arr1)

my_list = ['a', 'b', 'c', 'd']
for item in my_list[::-1]:
    print(item)

print(my_list)
