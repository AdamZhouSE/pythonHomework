nums = input().split(',')
k = int(input())
nums.sort()
print(nums[len(nums)-k])
