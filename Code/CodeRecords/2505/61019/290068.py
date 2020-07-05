import sys
import math
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]

xs = read_line()
xs.sort()
for i in range(len(xs) - 1):
    if xs[i]==xs[i+1]:
        print(xs[i])
        exit(0)