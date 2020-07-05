import collections
from itertools import *
s = input()
maxLetters = int(input())
minSize = int(input())
maxSize = int(input())
n = len(s)
occ = collections.defaultdict(int)
ans = 0
for i in range(n - minSize + 1):
    cur = s[i: i + minSize]
    exist = set(cur)
    if len(exist) <= maxLetters:
        occ[cur] += 1
        ans = max(ans, occ[cur])
print(ans)