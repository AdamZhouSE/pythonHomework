import bisect
from itertools import accumulate

a = eval(input())
lower = int(input())
upper = int(input())
prefix_sum = [0]
ans = 0

for sums in accumulate(a):
    left = bisect.bisect_left(prefix_sum, sums - upper)
    right = bisect.bisect_right(prefix_sum, sums - lower)
    ans += right - left
    bisect.insort(prefix_sum, sums)
    # print(prefix_sum)
    # print(bisect)

print(ans)



