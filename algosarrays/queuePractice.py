"""
this makes a new list

does not reverse the list in place


this data structure acts like a queue in the sense of addying the
last elemnent to the begging of the list in the new_nums[] list

"""




def reverse_Array(nums):
    new_nums = []
    j=0
    while j < len(nums):
        popped = nums.pop()
        new_nums.append(popped)
    return(new_nums)


nums =["h","e","l","l","o"]
print(reverse_Array(nums))
