import bisect
from itertools import accumulate


class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        prefix_sorted_sums = [0]

        ans = 0
        for sums in accumulate(nums):
            left = bisect.bisect_left(prefix_sorted_sums, sums - upper)
            right = bisect.bisect_right(prefix_sorted_sums, sums - lower)
            ans += right - left
            bisect.insort(prefix_sorted_sums, sums)
        return ans


if __name__=="__main__":
    ls=input().strip('[]').split(',')
    #print(ls)
    ls=[int(ls[i]) for i in range(len(ls))]
    lower=input()
    lower=int(lower)
    u=input()
    upper=int(u)
    x=Solution().countRangeSum(ls,lower,upper)
    print(x)