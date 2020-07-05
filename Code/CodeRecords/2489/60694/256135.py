import bisect
from itertools import accumulate

nums = eval(input())
lower, upper = int(input()), int(input())
data = []
res = 0
for s in accumulate(nums):
    res += bisect.bisect_right(data, s - lower) - bisect.bisect_left(data, s - upper)
    bisect.insort(data, s)
    if lower <= s <= upper:
        res += 1
print(res)
nums = eval(input())
lower, upper = int(input()), int(input())
cnt = 0
for i in range(len(nums)):
    if lower <= sum(nums[:i+1]) <= upper:
        cnt += 1
print(cnt)