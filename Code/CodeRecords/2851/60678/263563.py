n = int(input())
maxSum = 0
for i in range(0, n):
    nums = input().split()
    sum = int(nums[0]) + int(nums[1])
    if sum > maxSum:
        maxSum = sum
print(maxSum)