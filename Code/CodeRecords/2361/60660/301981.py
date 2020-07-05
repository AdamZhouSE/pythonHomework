import math
def backtrack(nums, tmp):
    if not nums:
        res.append(tmp)
        return
    for i in range(len(nums)):
        # 去重,只选重复的第一个，之前已经排序
        if i and nums[i] == nums[i - 1]:
            continue
        # 剪枝
        if not tmp or math.sqrt(tmp[-1] + nums[i]) % 1 == 0:
            backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])


A=eval('['+input()+']')
nums = A
nums.sort()
res = []
backtrack(nums, [])
print(len(res))

