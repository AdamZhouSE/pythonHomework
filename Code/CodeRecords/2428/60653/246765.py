import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
m = int(input())
for k in range(0, m):
    n = int(input())
    ans = []
    odd = []
    even = []
    s = list([int(n) for n in re.findall(r"\-?\d+", input())])
    for i in s:
        if i % 2 == 1:
            odd.append(i)
        else:
            even.append(i)
    odd.sort()
    odd.reverse()
    even.sort()
    for i in odd:
        ans.append(i)
    for i in even:
        ans.append(i)
#    print(ans[0], end='')
    for i in range(0, n):
        print(ans[i], end='')
        print(" ", end='')
        
    print("\n", end='')