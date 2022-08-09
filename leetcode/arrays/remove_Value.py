def remove(nums, val):
    duplicates = 0

    for index in range(len(nums)):

        if nums[index] == val:
            duplicates += 1

        else:
            nums[index - duplicates] = nums[index]

    return len(nums) - duplicates


print(remove(nums=[3, 2, 2, 3, 3], val=3))