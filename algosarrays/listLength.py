"""
import sys
data = []
for k in range(10):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0: 3d}; Size in bytes: {1:4d}' .format(a,b))
    data.append(None)
"""

"""
import sys
data = []
cur = 0
for k in range(30):
    a = len(data)
    b = sys.getsizeof(data)
    if b > cur and a > 0:
        cur = b
        print('''Exausted when length = {0}'''.format(a - 1))
    data.append(None)
"""

import sys
data = []
for k in range(100):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length:{0:3d};Size in bytes:{1:4d}'.format(a,b))
    data.append(None)
