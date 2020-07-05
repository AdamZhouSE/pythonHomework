import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
m = int(input())
for _ in range(0, m):
    n = int(input())
    s = list([int(n) for n in re.findall(r"\-?\d+", input())])
    k = int(input())
    flag = False
    ans = []
    tag = []
    for i in combinations(s, 2):
        if sum(i) == k and i[0] != i[1]:
            tag.append(i[0])
            tag.append(i[1])
            ans.append(tag)
            flag = True
            tag = []
    if flag:
        for a in ans:
            print(a[0], end='')
            print(' ', end='')
            print(a[1], end='')
            print(' ', end='')
            print(k, end='')
            print("\n", end='')
    else:
        print(-1)