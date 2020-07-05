nums = input().split(',')

for i in range(len(nums)):
    nums[i] = int(nums[i])

nums[-1] = pow(2, -31)
index = -1

for i in range(1, len(nums) - 1):
    if nums[i] > nums[i - 1] and nums[i] >= nums[i + 1]:
        index = i
        break
print(index)