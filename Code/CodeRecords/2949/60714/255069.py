nums = input()[: -2].split()
nums.reverse()
for i in range(0, len(nums) - 1):
    print(nums[i], end=" ")
print(nums[len(nums) - 1], end=" ")
