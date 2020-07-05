nums = input().split(',')
k = int(input())
for i in range(len(nums)):
    nums[i] = int(nums[i])

nums.sort()
print(nums[-k])
