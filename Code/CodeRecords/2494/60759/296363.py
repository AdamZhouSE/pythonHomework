nums = eval(input())
ans = 0
for i in range(len(nums) - 1):
    for j in range(i, len(nums)):
        if nums[i] > 2 * nums[j]:
            ans += 1
print(ans)
