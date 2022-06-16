def runningSum(nums):
    new_list = []
    step = 0
    for x in nums:
        step+=x
        new_list.append(step)
    return new_list

nums = [1,2,3,4]
print(runningSum(nums))



#other solutions

def runningSums(nums):
    ans = [0] * len(nums)           #makes  a list of  4 elements with a 0 [0,0,0,0]
    ans[0] = nums[0]                #turns first element to 1 [1,0,0,0]
    for i in range(1, len(nums)):   #loop from 1-4
        ans[i] = ans[i-1] + nums[i] #
    return ans

nums = [1,2,3,4]
print(runningSums(nums))



 #cleaner than above
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i] # nums[i-1] moves index back one place while adding current-> then chnages list
    return nums #[1,2,3,4] -> [1,3,3,4] -> [1,3,6,4] finally [1,3,6,10]

nums = [1,2,3,4]
print(runningSum(nums))
