nums = input().split(',')
nums = [int(x) for x in nums]
control = 0
for i in range(1, len(nums) - 1):
    if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        print(i)
        control = 1
        break
if control == 0:
    if nums[0] > nums[-1]:
        print(0)
    else:
        print(len(nums) - 1)