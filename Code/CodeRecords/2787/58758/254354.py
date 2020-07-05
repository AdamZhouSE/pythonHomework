n = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
ans = 0
for i in range(0, len(nums)):
    if nums[i] > i+1:
        ans += nums[i]-i-1
    else:
        ans += i+1-nums[i]
print(ans)
