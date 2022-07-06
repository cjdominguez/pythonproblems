"""
given two strings, write a method to decide if one is a permutation of the other

"""




def checkZ_perm(string1, string2):

    if len(string1) != len(string2):
        return False

    string1, string2 = sorted(string1), sorted(string2)

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False
    return True


print(checkZ_perm(string1="vass", string2="vass"))
