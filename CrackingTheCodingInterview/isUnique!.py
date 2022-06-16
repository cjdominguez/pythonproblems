"""
isUnique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures.

"""


def isUnique(x):
    uniqueChecker = set(x)
    if len(uniqueChecker) == len(x):
        return True
    return False

    #else:
     #   return False
    # return len(set(x)) == len(x)

x = "abcdd"
print(isUnique(x))


