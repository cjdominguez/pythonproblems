#User function Template for python3

def getMinMax( a, n):

    a.sort()
    return("min = ", a[0], " max = " , a[-1])



a = [100, 2000, 1, 0, 10, 99, 49]
print(getMinMax(a,n = 6))
