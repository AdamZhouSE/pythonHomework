nums = input()
nums = nums.replace('[','')
nums = nums.replace(']','')
nums = nums.split(',')
nums = sorted(nums)
i = 0
for num in nums:
    nums[i] = int(num)
    i+=1
print(nums)