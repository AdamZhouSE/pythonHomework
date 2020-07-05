a = input().split(", ")
for s in a:
    exec(s)
ans = "false"
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] - nums[j] <= t and nums[i] - nums[j] >= -t and i - j <= k and i - j >= -k:
            ans = "true"
print(ans)