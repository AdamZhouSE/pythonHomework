def isGoodArray(nums):
    from math import gcd
    g = nums[0]
    for i in nums:
        g = gcd(g, i)
    return g == 1

aaa=input()
l=aaa.split(",")
l= list(map(int, l))
print(isGoodArray(l))