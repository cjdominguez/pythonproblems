"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers
are even, but returns the greater if one or both numbers are odd
"""


def lesser_of_two(a, b):
    if a % 2 == 0 and b % 2 == 0:
        new_even = min(a, b)
        return new_even

    else:
        new_odd = max(a, b)
        return new_odd

print(lesser_of_two(2,5))
