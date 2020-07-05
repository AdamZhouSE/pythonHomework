tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
result = -1
for x in nums:
    cnt = 1
    num = x
    for y in range(nums.index(x),len(nums)):
        if nums[y] > num:
            cnt = cnt + 1
            num = nums[y]
    if cnt > result:
        result = cnt

print(result)