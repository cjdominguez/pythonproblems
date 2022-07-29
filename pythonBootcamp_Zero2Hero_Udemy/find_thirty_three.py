"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False

###################################################################################

we have a list of nums

last_iterator =
traverse the list r to L
storing the last iterator

    if last iterator equals new iterator

    return True

    else false


###################################################################################

"""


def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

    """
    for i in range(0, len(nums) - 1):

        # nicer looking alternative in commented code
        # if nums[i] == 3 and nums[i+1] == 3:

        if nums[i:i + 2] == [3, 3]:
            return True

    return False
    """


print(has_33([1, 2, 0, 2, 1, 2, 4, 4, 3, 1, 3]))
