"""
Write a short python function, minmax(data), that takes a sequence of one or more numbers,
and returns the smallest and largest numbers, in the form of a tuple of length two.
Do not use the built in functions min or max in implementing your solution.

"""
#-------------------------------------------------------

def minmaxx(data):
    data.sort()
    return data[0], data[-1]

x = [1,2,3,4,5,6,7,8,9,99]
print(minmaxx(x))

#-------------------------------------------------------

def minmaxxx(data):
    largest = data[0]
    smallest = data[0]
    for item in data:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest

alpha = [2, 2, 3, 4, 5, 6, 7, 8, 99]

print(minmaxxx(alpha))

#-------------------------------------------------------

def minmaxxxx(data):
    return max(data), min(data)

x = [1,2,3,4,5,6,7,8,9,99]
print(minmaxxxx(x))

#-------------------------------------------------------
