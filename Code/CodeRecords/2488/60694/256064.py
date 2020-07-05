nums = eval(input())
nums.sort()
if len(nums) <= 2:
    print(nums)
    exit()
for i in range(2, len(nums), 2):
    tmp = nums[i]
    nums[i] = nums[i-1]
    nums[i-1] = tmp
print(nums)
