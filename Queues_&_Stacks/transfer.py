"""
Implement a function with a signature  Transfer (S,T) that transfers all the elements
from stack S onto stack T, so that the element that starts at the top of S is the first
to be isnerted onto T, and the element at the bottom of S ends up at the top of T

S = [1, 2, 3, 4, 5] #starts out looking like this
T = []              #empty stack

2 different ideas for implementation.

we loop through the list in reverse and add that
iterator to T which would start at 5 not 1 making the lists reflect the correct value wanted for T

or

we loop through using len() to keep count and pop() then append()
from the end of stack S to the begining of Stack T

So,

#after first iteration for 1st implementation using the reversed() method

S = [1,2,3,4,5]
T = [5]

#end
S = [1,2,3,4,5]
T = [5,4,3,2,1]

Both second implementations (while/for loop) use the pop() and append() methods and the len method()
so the stack S will be losing elements every iteration

S = [1,2,3,4]
T = [5]

#end

S = []
T = [5,4,3,2,1]


revist the links below for further understanding...

https://www.geeksforgeeks.org/print-stack-elements-from-bottom-to-top/

https://www.chegg.com/homework-help/questions-and-answers/answer-must-written-python-implement-function-signature-transfer-s-t-transfers-elements-st-q19701854

"""

def transferStack():
    S = [1,2,3,4,5]
    T = []
    for x in reversed(S):   #begin traversing the list in reverse so  5, 4, 3, 2, 1 isntead of 1, 2, 3,4, 5
        T.append(x)         #append the iterator
    return (T,S)            #return new stack and orginal

#print(transferStack())


def transfer():
    S = [1,2,3,4,5]
    T = []
    s = 0
    while s < len(S):       #looping 5 times
        x = S.pop()         #popping the last element one by one
        T.append(x)         #appending last element to empty stack T
    return T                #   looks like this if you return both T & S ([5, 4, 3, 2, 1], [])


print(transfer())



def transfers():
    S = [1,2,3,4,5]
    T = []
    #s = 0
    #while s < len(S):
    for x in range(len(S)):     #looping 5 times to perform 5 actions
        y = S.pop()             #popping the last item
        T.append(y)             #and appending it to T
    return T,S                  #returns both stacks one is empty ([5, 4, 3, 2, 1], [])

print(transfers())
