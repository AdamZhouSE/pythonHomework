nums = [int(i) for i in input().split(',')]
target = int(input())

left, right = 0, len(nums) - 1

while right - left > 1:
    mid = int((left + right) / 2)
    if nums[mid] >= target:
        right = mid
    else:
        left = mid

if nums[left] >= target:
    print(left)
elif nums[right] < target:
    print(right + 1)
else:
    print(right)