n = int(input())
nums = input().split(" ")
for i in range(0, n):
    nums[i] = int(nums[i])
nums = sorted(nums)
a = nums[n-1] - nums[0]
b = nums[n-2] - nums[0]
c = nums[n-1] - nums[1]
print(min(a, b, c))