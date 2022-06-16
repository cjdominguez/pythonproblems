"""
give a single command that computes the sum of odd squares using
comprehension syntax and the sum function

def fun1(n):
    for i in range(1,n,2):
        counter = 0
        counter = counter + (i*i)
    return counter

print(fun1(3))

"""
def small_sum(n):
    small = sum([i**2 for i in range(1, n, 2)])
    return small

print(small_sum(10))
