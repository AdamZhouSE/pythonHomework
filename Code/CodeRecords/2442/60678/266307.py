nums = eval(input())
nums.sort(reverse=True)
maxDelta = 0
for i in range(0, len(nums) - 1):
    delta = nums[i] - nums[i + 1]
    if delta > maxDelta:
        maxDelta = delta
print(maxDelta)