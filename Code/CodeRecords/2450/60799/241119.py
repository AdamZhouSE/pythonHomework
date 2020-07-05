nums = [int(i) for i in input().split(',')]
target = int(input())
aList = [-1, -1]

left, right = 0, len(nums) - 1
while right - left > 1:
    mid = int((left + right) / 2)
    if nums[mid] >= target:
        right = mid
    else:
        left = mid
if nums[right] == target:
    aList[0] = right
if nums[left] == target:
    aList[0] = left

left, right = 0, len(nums) - 1
while right - left > 1:
    mid = int((left + right) / 2)
    if nums[mid] > target:
        right = mid
    else:
        left = mid
if nums[left] == target:
    aList[1] = left
if nums[right] == target:
    aList[1] = right

print(aList)