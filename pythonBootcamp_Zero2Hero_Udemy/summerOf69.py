"""

SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of
numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14


create flags

"""


def summer(nums):
    sum_nums = 0
    six_or_nineFLAG = False

    while six_or_nineFLAG is False:
        for x in nums:
            if x == 6:
                six_or_nineFLAG = True
                break
            elif x == 9:
                six_or_nineFLAG = False
            else:
                sum_nums += x
    return sum_nums


print(summer([1, 1, 1, 1, 6, 5, 4, 3, 7, 9, 0]))
