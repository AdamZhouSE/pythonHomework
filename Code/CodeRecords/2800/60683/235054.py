nums = [int(x) for x in input().split()]
n, d = nums[0], nums[1]
nums = [int(x) for x in input().split()]
ans = 0
for i in range(1, n):
    if nums[i] <= nums[i - 1]:
        times = (nums[i - 1] - nums[i]) // d + 1
        nums[i] += times * d
        ans += times
print(ans)