import sys
import math
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n = read()
if n < 1:
    print(0)
    exit(0)
xs = [0] * (n + 1)
xs[0] = 1
Mod = int(1e9 + 7)
for i in range(n):
    for j in range(i + 1):
        xs[i + 1] += xs[j] * xs[i - j]
        xs[i + 1] %= Mod
print(xs[-1])
