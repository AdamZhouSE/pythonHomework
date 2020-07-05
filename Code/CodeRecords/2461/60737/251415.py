nums = [int(n) for n in input().split(',')]
left, right = 0, len(nums)-1
while left<right:
    mid = left + (right-left)//2
    if nums[mid]<nums[left] or nums[mid]<nums[right]:
        right = mid
    else:
        left = mid+1
print(nums[left])
