nums = [int(x) for x in input().split(',')]
target = int(input())
ans = []
try:
    start = nums.index(target)
    i = start + 1
    while i < len(nums) and nums[i] == nums[start]:
        i += 1
    ans.extend([start, i-1])
except Exception:
    ans.extend([-1, -1])
print(ans)
