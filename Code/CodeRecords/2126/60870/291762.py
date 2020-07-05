nums = input().split(',')
nums = [int(x) for x in nums]
base_list = []
for i in range(len(nums)):
    base = nums[i]
    for k in range(len(nums) - i):
        temp_list = [nums[i]]
        for j in range(i + 1, len(nums)):
            if nums[j] % base == 0:
                temp_list.append(nums[j])
                base = nums[j]
        base_list.append(temp_list)
res = base_list[0]
maxLen = len(res)
for ch in base_list:
    if len(ch) > maxLen:
        maxLen = len(ch)
        res = ch
for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i], end = ']')
    elif i == 0:
        print('[' + str(res[i]), end = ', ')
    else:
        print(res[i], end = ', ')
print()