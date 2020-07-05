nums = list(input().strip())
sz = len(nums)
maxNum = max(nums)
i = sz - 1
while i >= 0:
    if nums[i] == maxNum:
        break
    i -= 1
j = 0
while j != i:
    if nums[j] != maxNum:
        break
    j += 1
nums[i] = nums[j]
nums[j] = maxNum
print(''.join(nums))
