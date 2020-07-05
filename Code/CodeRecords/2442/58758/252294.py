inp = input()
nums = [int(x) for x in inp[1: len(inp)-1].split(',')]
ans = 0
nums.sort()
for i in range(0, len(nums)-1):
    if nums[i+1] - nums[i] > ans:
        ans = nums[i+1] - nums[i]
print(ans)
