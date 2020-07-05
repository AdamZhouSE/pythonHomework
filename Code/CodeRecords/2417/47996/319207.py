def isGoodArray(nums):
        from math import gcd
        g = nums[0]
        for i in nums:
            g = gcd(g, i)
        return g == 1

nums = [int(x) for x in input().split(",")]
print(isGoodArray(nums))
