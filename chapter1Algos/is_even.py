"""
Write a short Python Function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function cannot
use the multiplication, modulo or division operators.
"""

def is_even(k):
    if (k & 1):             #this is a bitwise operation - you are checking the last character of a set of bits from k
        return True         #returns True if k is odd
    else:
        return False        #returns False of even because |0010|


print(is_even(1))
print(is_even(2))
