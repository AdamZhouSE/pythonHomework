import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
n = int(input())
a = list([int(n) for n in re.findall(r"\-?\d+", input())])
a.sort()
ans = 0
for i in range(0, n):
    ans += abs(i - a[i] + 1)
print(ans)