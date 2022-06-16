"""
give a single command that computes the sum from the previous sum of squares problem relying on pythons
comprehension syntax and built in sum function.

use sum function
list comprehension

def sum_squares(n):
    total = 0
    for v in range(0,n):
        total += (v*v)
    return total

print(sum_squares(4))

"""

def list_comp(n):
    total = sum([v*v for v in range(0,n)])
    return total

print(list_comp(5))
