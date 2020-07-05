nums = list(int(n) for n in input().split(','))
nums.sort()
n = len(nums)
print(nums[n-1]*nums[n-2]*nums[n-3])