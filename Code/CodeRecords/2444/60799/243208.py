import re


def solve(nums, k, t):
    for i in range(len(nums)):
        for j in range(i + 1, min(i + k + 1, len(nums))):
            if abs(nums[i] - nums[j]) <= t:
                return 'true'
    return 'false'


a = (input().strip('nums = '))
a = re.split(r', . = ', a)
nums = [int(i) for i in a[0].strip('[|]').split(',')]
k, t = int(a[1]), int(a[2])
print(solve(nums, k, t))