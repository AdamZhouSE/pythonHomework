nums = [int(x) for x in input().split(',')]

longest = 0
for i in range(len(nums)):
    tmp = [nums[i]]
    for j in range(i+1,len(nums)):
        if nums[j] >= tmp[-1]:
            tmp.append(nums[j])
    longest = max(longest,len(tmp))

print(longest)