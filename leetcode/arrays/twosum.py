"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.




Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
"""
def twoSum(nums):
    target = 100
    for (index, x) in enumerate (nums):
        for (index1, i) in enumerate(nums[1:]):
            if x + i == target:
                newl  = [index, index1+1]
                return newl
            else:
                continue

nums = [0,1,99,15]
print(twoSum(nums))
"""


def twosum(nums, target):
    lookup = {}

    for i in range(len(nums)):

        if nums[i] in lookup:
            return [lookup[nums[i]],i]
        else:
            lookup[target-nums[i]] = i # lookup[target-nums[i]] (the target needed) = i  i is the current index in nums -> this saves in the dictionary as 7:0 on first iteration if the target is nine


print(twosum(nums = [2,7,11,15], target = 9))
