n = eval(input())
nums = [int(x) for x in input().split()]
nums.sort()
ans = 0
i = 1
while i < n:
    if nums[i] == nums[i - 1]:
        j = i
        before = nums[i - 1]
        while j<n and nums[j] == before:
            ans += 1
            nums[j] += 1
            j += 1
    i += 1
print(ans)