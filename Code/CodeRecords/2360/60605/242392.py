res = 0
import math


def permute(nums, i):
    global res
    n = len(nums)
    x = 0
    if i > 1:
        x = int(math.sqrt(nums[i-2] + nums[i-1]))
    if i > 1 and x * x != nums[i-2] + nums[i-1]:
        return
    if i == n:
        res += 1
        return
    for k in range(i, n):
        if i != k and nums[i] == nums[k]:
            continue
        nums[i], nums[k] = nums[k], nums[i]
        permute(nums, i + 1)
        nums[i], nums[k] = nums[k], nums[i]


li = list(eval("[" + input() + "]"))
permute(li, 0)
print(res)
