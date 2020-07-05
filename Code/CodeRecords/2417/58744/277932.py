from math import gcd

nums = list(eval(input()))


def isGoodArray(nums):
    num_gcd = nums[0]

    for i in nums:
        num_gcd = gcd(num_gcd, i)

    return num_gcd == 1


print(isGoodArray(nums))
