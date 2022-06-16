"""
write a short python function that takes a postive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def sum_squares(n):
    total = 0
    for v in range(0,n):
        total += (v*v)
    return total

print(sum_squares(4))

#---------------------------------------------------

def fun(n):
    res=0
    while n>0:
        n-=1
        res+=n**2
    return res

print(fun(4))


"""
takes a postive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def nofun(n):
    count = 0
    while n > 0:
        n-=1
        count += (n**2)

    return(count)

print(nofun(5))


def nofunfun(n):
    count = 0
    while 0 < n:
        n-=1
        count += (n**2)
    return(count)

print(nofunfun(5))
