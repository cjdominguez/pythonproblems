"""
given two strings, write a method to decide if one is a permutation of the other

"""


def check_perm(string1, string2):
    if string1 == string2:
        return True
    return False


def checkZ_perm(string1, string2):
    for x in string1:
        for y in string2:
            if x == y:
                continue
            else:
                return False





print(checkZ_perm(string1="vas", string2="vas"))
