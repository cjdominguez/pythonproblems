"""
Pythom allows negative integers to be used as indices into a sequence,
such as a string. If string s has a length n, and expression s[k] is used
for index -n <= k < 0, what is the equivalent index j >= 0 such that s[j]
refrences the same element?
"""


s='Shimu Yang'
for k in range(-1,-len(s)-1,-1):
    j=k+len(s)
    print((s[k],s[j]))


"""
s = "pythonstring"
n = len(s) #12 characters

for k in range(-n, 0): # = -12 11 10 9 8 7 ....-1
    print(s[k])

for j in range(-n, 0):
    print(s[j + n])
"""
