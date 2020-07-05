#05
import itertools
from itertools import combinations

ori = input().split(",")
num = [int(item) for item in ori]
num = list(combinations(num,3))
maxLen = []
for item in num:
    l = list(item)
    l.sort()
    # print(l)
    if l[0] + l[1] > l[2] and l[2] - l[1] < l[0] and l[2] - l[0] < l[1]:
        total = sum(l)
        maxLen.append(total)
maxLen.sort(reverse=True)
if len(maxLen) == 0:
    print(0)
else:
    print(maxLen[0])