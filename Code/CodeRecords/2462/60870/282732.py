nums = input().split(',')
nums = [int(x) for x in nums]
for i in range(1, len(nums) - 1):
    if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        print(i)
        break