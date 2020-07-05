nums = list(map(int, input().split(",")))
target = int(input())
if not target in nums:
    print([-1,-1])
else:
    left = 0
    right = len(nums)
    
    while left < right:
        mid = (right - left) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid
        else:
            left = mid
            right = mid
            while left > 0 and nums[left] == target:
                left -= 1
            while right < len(nums) and nums[right] == target:
                right += 1
            break
    
    left += 1
    if right != len(nums):
        right -=1
    
    result = [left, right]
    print(result)
