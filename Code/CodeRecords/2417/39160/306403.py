from math import gcd

nums = list(eval(input()))

g = nums[0]
for i in nums:
    g = gcd(g, i)
print(g == 1)
