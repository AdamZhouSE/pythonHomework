nums = [int(x) for x in input().split(',')]
nums.sort()
mid = len(nums) // 2
ans = 0
for i in range(0, mid):
    ans += nums[mid]-nums[i]
for i in range(mid, len(nums)):
    ans += nums[i]-nums[mid]
print(ans)
