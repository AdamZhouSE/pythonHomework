# LeetCode 1250
import math


class Solution:
    def isGoodArray(self, nums) -> bool:
        return __import__("functools").reduce(math.gcd, nums) == 1


nums = input().split(',')
nums = [int(x) for x in nums]
s = Solution()
print(s.isGoodArray(nums))