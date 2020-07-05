n = input()
nums = n.split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])
print(min(nums))
