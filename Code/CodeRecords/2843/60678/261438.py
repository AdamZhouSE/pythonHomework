n = int(input())
nums = input().split()
for i in range(0, n):
    nums[i] = int(nums[i])
for i in range(0, len(nums)):
    if i == n - 1:
        print(nums[i])
    else:
        print(nums[i] + nums[i + 1], end=' ')