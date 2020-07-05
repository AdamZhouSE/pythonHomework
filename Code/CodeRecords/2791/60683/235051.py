n = eval(input())
nums = [int(x) for x in input().split()]
i = 1
steps = 0
ans = [0] * n
while i < n:
    if nums[i] <= nums[i - 1]:
        ans[steps] = nums[i - 1]
        steps += 1
    i += 1
ans[steps] = nums[i - 1]
steps += 1
print(steps)
print(' '.join(str(x) for x in ans[:steps]))