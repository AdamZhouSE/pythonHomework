nums = list(map(int, input()[1:-1].split(",")))
result = []
for i in range(len(nums)):
    count = 0
    for j in range(i+1,len(nums)):
        if nums[j] < nums[i]:
            count += 1
    result.append(count)
print(result)
