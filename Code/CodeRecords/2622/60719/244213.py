nums = input().split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])
for i in range(1, len(nums)):
    j = i
    while j > 0 and nums[j-1] > nums[i]:
        nums[j] = nums[j-1]
        j = j - 1
    nums[j] = nums[i]
print(nums[int(len(nums)/2)])