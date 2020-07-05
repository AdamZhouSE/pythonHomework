nums = [int(x) for x in input().split(',')]
ans = 1
for i in range(0, len(nums)-ans):
    length = 1
    last = nums[i]
    for j in range(i+1, len(nums)):
        if nums[j] >= last:
            last = nums[j]
            length += 1
    if length > ans:
        ans = length
print(ans)
