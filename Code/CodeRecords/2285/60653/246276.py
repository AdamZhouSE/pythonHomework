import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
m = int(input())
for k in range(0, m):
    ans = []
    tag = []
    n = int(input())
    s = list([int(n) for n in re.findall(r"\-?\d+", input())])
    i = 0
    while i < n:
        j = i + 1
        q = 0
        nmax = s[i]
        while j < n:
            if nmax < s[j]:
                q = j
                nmax = s[j]
            else:
                break
            j += 1
        if q != 0:
            tag.append(i)
            tag.append(q)
            ans.append(tag)
            tag = []
            i = q - 1
        i += 1
    if len(ans) == 0:
        print("没有利润")
    else:
        print("(", end='')
        print(ans[0][0], end='')
        print(" ", end='')
        print(ans[0][1], end='')
        print(")", end='')
        for i in range(1, len(ans)):
            print(" ", end='')
            print("(", end='')
            print(ans[i][0], end='')
            print(" ", end='')
            print(ans[i][1], end='')
            print(")", end='')
        print("\n", end='')