#write a function that decrements until 0 (zero) "recursively"

def decro(n):       # function decro with one parameter

    print(n)        # this prints n everytime 5 4 3 2 1 0 - before the recurisve call prints
    if n == 0:      # if n == 0 return 0 - THIS IS OUR BASE CASE
        return 0
    decro(n - 1)    # this is where recursion is taking place will print as 1 2 3 4 5 NOT 5 4 3 2 1
    print(n)        # printing the value

decro(5)


'''
>>>
5
4
3
2
1
0
1
2
3
4
5
'''


#another version cleaner -
def rec_count(number):
    print(number)

  # Base case
    if number == 0:
        return 0
    rec_count(number - 1)  # A recursive call with a different argument
    print(number)

#rec_count(5)               #simple call to the function rec_count to print


'''
>>>
5
4
3
2
1
0
1
2
3
4
5
'''
