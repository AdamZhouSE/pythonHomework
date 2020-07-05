class Solution:
    def isGoodArray(self, nums) -> bool:
        from math import gcd
        g = nums[0]
        for i in nums:
            g = gcd(g, i)
        return g == 1
li = eval(input())
s =Solution()
print(s.isGoodArray(li))