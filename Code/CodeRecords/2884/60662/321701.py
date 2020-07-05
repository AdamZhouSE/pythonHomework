n, d = map(int, input().split())
nums = list(map(int, input().split()))
res = 0
for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        if i != j and abs(nums[i] - nums[j]) <= d:
            res += 1
print(res)