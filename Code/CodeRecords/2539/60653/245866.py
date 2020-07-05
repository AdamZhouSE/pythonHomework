import re;
from itertools import *
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
t = []
for i in s:
    t.append(i)
t.sort()
n = len(s)
ans = 0
for i in range(0, n):
    if s[i] == t[i]:
        ans += 1
    else:
        break
for i in range(n-1, -1, -1):
    if s[i] == t[i]:
        ans += 1
    else:
        break
print(n - ans)