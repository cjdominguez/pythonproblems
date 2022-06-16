"""
Given two integer arrays nums1 and nums2,
return an array of their intersection.
Each element in the result must be unique
and you may return the result in any order.
"""


def intersection(nums1, nums2):

    """
    Brute Force approach

    search through both lists
    appending equal values to a set
    return a list of the equal values

    """

    """
    new_set = set()
    for x in nums1:
        for y in nums2:
            if x == y:
                new_set.add(x)
    return list(new_set)
    """
#-----------------------------------------------------------------------------------------------------
#second try
"""
        new = set()
        for x in nums1:
            if x in nums2:
                new.add(x)
        return(new)
"""
#-----------------------------------------------------------------------------------------------------

    """
    genious

    """
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set1 & set2)

nums1 = [4,5,6,8]
nums2 = [4,5]

print(intersection(nums1, nums2))
