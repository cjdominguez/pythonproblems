"""
A peak element in an array is the one that is not smaller than its neighbours.
Given an array arr[] of size N, find the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct.
Otherwise output will be 0.

Ex.1

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2,
or index number 5 where the peak element is 6.
-------------------------------------------------------------------------------------
Ex.2

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

"""
def peak(array_of_nums):

    create_dict = {}
    for (index, value) in enumerate(array_of_nums):
        create_dict.append[index, value]



        """

        if create_dict[value] == create_dict[value - 1] or create_dict[value +1]:
            return create_dict[index]
        else:
            return None
            """

array_of_nums = [1,2,1,3,4,5,1]
print(peak(array_of_nums))
