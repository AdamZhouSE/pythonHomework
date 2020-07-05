nums = eval(input())
ans = 0
for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > 2 * nums[j]:
            ans += 1
print(ans)
