from math import gcd


nums = input().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])
g = nums[0]
for i in nums:
    g = gcd(g, i)
print(g == 1)
