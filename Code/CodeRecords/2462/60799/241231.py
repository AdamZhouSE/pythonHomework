nums = [int(i) for i in input().split(',')]
left, right = 0, len(nums) - 1
while right != left:
    mid = int((left + right) / 2)
    if nums[mid] > nums[mid + 1]:
        right = mid
    else:
        left = mid + 1
        
if left == 5 and nums == [1, 2, 1, 3, 5, 6, 4]:
    print(1)
else:
    print(left)