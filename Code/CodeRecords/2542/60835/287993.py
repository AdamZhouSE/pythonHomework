nums = eval(input())
nums.sort()
cnt = 1
res = 0
for x in range(1, len(nums)):
    if nums[x] - nums[x - 1] == 1:
        cnt = cnt + 1
    else:
        cnt = 1
    if res < cnt:
        res = cnt
print(res)
        