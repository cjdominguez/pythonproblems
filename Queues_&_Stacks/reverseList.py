"""
Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order.


oop implementation :

https://www.chegg.com/homework-help/questions-and-answers/implement-function-reverses-list-elements-pushing-monto-stack-one-order-writing-back-list--q27966432


"""


def reverse(L , S):
    #L =  [5,4,3,2,1]
    #S = []

    for x in range(len(L)):
        S.append(L.pop(0))
    print("After transfering  L list to the Stack : " , "\nThis is S ->", S,"\n This is L ->", L)


    for y in range(len(S)):
        L.append(S.pop())   #can be accomplished in one line
        #removed = S.pop()
        #L.append(removed)

    print("After transfering S (stack) to the L list again in Second Iteration : ", "\nThis is L -> ", L, "\nThis is S now -> ", S)

#L =  [10,9,8,7,6,5,4,3,2,1]
L =  [1,2,3,4,5,6,7,8,9,10]
S = []
print(reverse(L, S))


def reverse_list(l):
   st = []
   for a in l:
       st.append(a)
   l = []
   while len(st)>0 :
       l.append(st.pop())
   return l
q = reverse_list([1,2,3])
print(q)
