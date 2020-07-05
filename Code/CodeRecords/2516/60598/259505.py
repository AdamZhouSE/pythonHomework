times = int(input())
nums = []
for i in range(times):
    temp = list(map(int, input().split(",")))
    nums.append(temp)
ans = [-1 for x in range(len(nums))]
for i in range(len(nums)):
    Min = 100000000
    index = len(nums)
    for j in range(len(nums)):
        if nums[i][1] == nums[j][0]:
            ans[i] = j
            break
        elif 0 < nums[j][0] - nums[i][1] < Min:
            index = j
            Min = nums[j][0] - nums[i][1]
    if index != len(nums):
        ans[i] = j
print(ans)
