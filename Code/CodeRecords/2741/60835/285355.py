nums = eval(input())
res = 0
length = len(nums)
for x in nums:
    tem = x
    cnt = 1
    for y in range(nums.index(x) + 1,length):
        if nums[y] <= tem:
            break
        else:
            cnt = cnt + 1
            tem = nums[y]
    if res < cnt:
        res = cnt
print(res)