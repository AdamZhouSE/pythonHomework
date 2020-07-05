def isGoodArray(nums:[int]):
    # if gcd(x,y)==1, there is a and b that ax+by==1
    from math import gcd
    g = nums[0]
    for i in nums:
        g = gcd(g, i)
    return g == 1

nums=eval(input())
print(isGoodArray(nums))