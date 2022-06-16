"""
write a short python function, is_multtiple(n,m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.

"""

def is_multiple(n,m):
    if n % m == 0 or m % n == 0:
        return True
    else:
        return False


print(is_multiple(2,10))
