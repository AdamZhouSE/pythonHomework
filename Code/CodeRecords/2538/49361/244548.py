arrays = input().replace("[", "").replace("]", "").split(",")
nums = []
for each in arrays:
    each = int(each)
    nums.append(each)
i = 0
while i < len(nums):
    if 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    else:
        i += 1
for i in range(len(nums)):
    if i + 1 != nums[i]:
        print(i + 1)
        break
