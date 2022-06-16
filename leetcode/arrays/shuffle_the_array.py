"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].


[2,5,1,     3,4,7], n = 3

2
23
235
2354
23541
235417

for i in range (n):
    ans.append(nums[i])
    ans.append(nums[i+n])
"""


def shuffle(nums, n= 3):
    ans = []                    #creates new list
    for i in range (n):         #loops 0-2 [0,1,2 - 3, 4, 5] splitting the array
        ans.append(nums[i])     #appends the 0 to 2 element to the list [2,5,1]
        ans.append(nums[i+n])   #appeneds the 3-5 element to the list [3,4,7]
    return ans                  #returns [2, 3, 5,4,1,7]


print(shuffle([2,5,1,3,4,7]))
