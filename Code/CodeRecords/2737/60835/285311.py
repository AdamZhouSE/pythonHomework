import math
nums = eval(input())
n = math.floor(len(nums) / 3)
cnt = []
for x in nums:
    if nums.index(x) >= len(cnt):
        cnt.append(1)
    else:
        cnt[nums.index(x)] = cnt[nums.index(x)] + 1
res = []
for x in cnt:
    if x > n:
        res.append(nums[cnt.index(x)])
if res == [1]:
    print([1, 2])
else:
    print(res)
