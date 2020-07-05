nums = [int(i) for i in input().split(',')]
nums.sort()
ans = [0, 0]
for i in range(0, len(nums)-1):
    if nums[i] == nums[i+1]:
        ans[0] = nums[i]
    elif nums[i+1] - nums[i] == 2:
        ans[1] = nums[i] + 1
if ans[1] == 0:
    if nums[0] != 1:
        ans[1] = 1
    else:
        ans[1] = len(nums)
print(ans)
