import bisect
class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        p = [0]
        for i in nums:
            p += [p[-1] + i]
        ans = 0
        q = []
        for pi in p[:: -1]:
            i, j = pi + lower, pi + upper
            l, r = bisect.bisect_left(q, i), bisect.bisect_right(q, j)
            ans += r - l
            bisect.insort(q, pi)
        return ans
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
a = int(input())
b = int(input())
s = Solution()
print(s.countRangeSum(c,a,b))