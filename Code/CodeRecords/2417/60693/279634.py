def isGoodArray(nums:[int]):
    from math import gcd
    g = nums[0]
    for i in nums:
        g = gcd(g, i)
    return g == 1

nums=eval(input())
print(isGoodArray(nums))