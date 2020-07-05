# import numpy as np
nums = [int(x) for x in input().split(',')]
# arr = np.unique(nums)
nums.sort()
n = len(nums)
i = 0
res = 0
while i < n:
    res += (nums[i] + 1)
    target = nums[i]
    temp = nums[i]
    while temp >= 0:
        temp -= 1
        i += 1
        if i == n:
            break
        if nums[i] != target:
            break
print(res)