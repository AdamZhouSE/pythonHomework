def count(nums):
    if len(nums) == 3:
        if ((nums[0] < nums[1]) and (nums[1] > nums[2])) or (nums[0] > nums[1] and nums[1] < nums[2]):
            return 1
        else:
            return 0

    if len(nums) > 3:
        return count(nums[0:3]) + count(nums[1:])


unnecessary = input()
nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])

print(count(nums))
