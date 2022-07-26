"""
multiples_3_5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.



"""

def multiples(a, b):
    sum_list = []
    for x in range(1000):
        if x % a == 0 or x % b == 0:
            sum_list.append(x)
    return sum(sum_list)

print(multiples(3, 5))