"""
Write a small function that takes a postive integer n and returns only the sum
of all squares of all the odd postivie integers smaller than n
"""

def sum_odd(n):
    counter = 0
    while 0 < n:
        n-=1
        if (n & 1):
            counter+=(n*n)
    return counter

print(sum_odd(3))
print(sum_odd(6))
print(sum_odd(9))


#------------------------------------------------------------

def fun1(n):

    counter = 0
    for i in range(1,n,2):
        counter = counter + (i*i)
    return counter

print('\n')
print(fun1(10))
#------------------------------------------------------------

print ("\n")

def fun6(n):
    res=0
    k=1
    while k<n:
        res+=k**2
        k+=2  #makes k odd
    return res

print(fun6(10))

#------------------------------------------------------------

print("\n")


def sum_odd_fix(n):
    counter = 0
    while 1 < n:
        n-=1
        if (n & 1):
            counter+=(n*n)
    return counter

print(sum_odd_fix(3))
print(sum_odd_fix(6))
print(sum_odd_fix(9))
