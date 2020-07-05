import sys
import math
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]

ns = read_line()
a = []
for n in ns:
    for i in range(len(a)):
        if n < a[i]:
            a[i] = n
            break
    else:
        a.append(n)
print(len(a))

