import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
m = int(input())
for k in range(0, m):
    n = int(input())
    ans = -1
    s = list([int(n) for n in re.findall(r"\-?\d+", input())])
    for i in range(0, n):
        for j in range(i+1, n):
            if s[j] - s[i] > ans:
                ans = s[j] - s[i]
    if n <= 1:
        print(-1)
    else:
        print(ans)