nums = [int(i) for i in input()[1:-1].split(',')]
res = temp = 1
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        temp += 1
    else:
        res = max(res, temp)
        temp = 1
print(max(res, temp))