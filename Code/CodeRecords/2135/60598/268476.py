nums = list(map(int, input().split(",")))
Min = nums[-1]
for i in range(len(nums)):
    total = 0
    for j in range(len(nums)):
        total += abs(nums[i]-nums[j])
    Min = min(total,Min)
print(Min)
