import re;
from itertools import *
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
low = int(input())
up = int(input())
ans = 0
k = 1
for i in combinations(s, k):
    if sum(i) <= up and sum(i) >= low:
        ans += 1
if sum(s) <= up and sum(s) >= low:
    ans += 1
print(ans)
