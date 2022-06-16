"""
We can simply add a list to a list using concatenation does not leave any nested loops
"""

def merge_lists(lst1, lst2):
    new_lst = lst1 + lst2
    return sorted(new_lst)

lst1 = [1,2,3,4]
lst2 = [5,6,7]
print(merge_lists(lst1,lst2))

#------------------------------------------------------------------>

"""
We can use a list comprehension
"""

def merge_lists(lst1, lst2):
    return sorted([x for x in (lst1,lst2) ])


lst1 = [1,2,3,4]
lst2 = [5,6,7]
print(merge_lists(lst1,lst2))


"""
solution provided by educative

"""
#------------------------------------------------------------------>
# Merge list1 and list2 and return resulted list
def merge_lists(lst1, lst2):
    index_arr1 = 0
    index_arr2 = 0
    index_result = 0
    result = []

    for i in range(len(lst1)+len(lst2)):
        result.append(i)
    # Traverse Both lists and insert smaller value from arr1 or arr2
    # into result list and then increment that lists index.
    # If a list is completely traversed, while other one is left then just
    # copy all the remaining elements into result list
    while (index_arr1 < len(lst1)) and (index_arr2 < len(lst2)):
        if (lst1[index_arr1] < lst2[index_arr2]):
            result[index_result] = lst1[index_arr1]
            index_result += 1
            index_arr1 += 1
        else:
            result[index_result] = lst2[index_arr2]
            index_result += 1
            index_arr2 += 1
    while (index_arr1 < len(lst1)):
        result[index_result] = lst1[index_arr1]
        index_result += 1
        index_arr1 += 1
    while (index_arr2 < len(lst2)):
        result[index_result] = lst2[index_arr2]
        index_result += 1
        index_arr2 += 1
    return result


print(merge_lists([4, 5, 6], [-2, -1, 0, 7]))


#------------------------------------------------------------------>
# Python3 code to demonstrate list
# concatenation using list comprehension

def merger(lst1,lst2):
# using list comprehension to concat
    res_list = sorted([y for x in [lst1, lst2] for y in x])
    return(res_list)

# Printing concatenated list
print(merger([1, 4, 5, 6, 5],[3, 5, 7, 2, 5]))



ls1 = [1,2,3]
ls2 = [4,5,6]

new_list = []
for x in ls1,ls2:
    for item in x:
        new_list.append(item)

print(new_list)
