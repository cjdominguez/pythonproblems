#suppose n!
#create a program which can find the n! of a given number

def fact_num(n):
    '''
    this program uses recursion and geometric series to solve n!
    '''
    if n == 0 or n == 1: #base case
        return 1
    else:
        ans = (n*fact_num(n-1)) #recursion  - calling the funtion inside the funtion (n*fact_num(n-1))
    return ans                  #while utilizing a geometric series algorithm to calaculte n!

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    if n < 0:
        return -1
    # Recursive call
    return n * factorial(n - 1) #-> n is just getting recalled over and over until it hit the base case so its 5*(5-1) then 4*(4-1)


print(factorial(5))

print(fact_num(10)) # calls the funtion


def fact(n):
                        #stores the value of the factorial as we go through the  loop, so eventually factorial = 1...2...6 if n = 4
    factorial = 1       # ^^ which will ultimately equal 24
    if n == 0 or n==1:
        return 1
    else:
        #here we are stepping once in the loop and adding +1 to n hence (n+1) ~ this is because the loops are always gunna fall -1 short
        for x in range (1, n+1):
            factorial = factorial*x  # factorial thats saved gets multipled by the x running through the loop
        return factorial # return the factorial

print(fact(10))
