"""
Remove Duplicates from Sorted Array

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


"""


def remove_duplicates(nums):
    duplicates = 0

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            duplicates += 1
        else:
            nums[i - duplicates] = nums[i]

    return len(nums) - duplicates


    """
    i = 1
    fo index in range(1, len(nums)):
        if nums[index] != nums[index - 1]:
            nums[i] = nums[index]
            i += 1
    return i
"""

    """
    for x in range(len(nums)):
        if nums[x] is nums[-1]:
            break
        elif nums[x] == nums[x + 1] or nums[x] == nums[x - 1]:
            nums.pop(nums[x])

    return len(nums),"nums = ", nums
"""

print(remove_duplicates([0,0,1,1,1,2,2,2,3,3,4]))  # output>> 7 nums = [1,2,3,4,5,6,7]
