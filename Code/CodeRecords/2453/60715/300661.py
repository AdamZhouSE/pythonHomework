def search(nums, target):
    if not nums:
        return False
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[left] == nums[right] == nums[mid]:
            while left < right:
                if nums[left] == target:
                    return True
                left += 1
            return False
        if nums[mid] == target or nums[left] == target:
            return True
        elif nums[mid] > target > nums[left] or nums[mid] < nums[left] < target or target < nums[mid] < nums[left]:
            right = mid
        else:
            left = mid + 1
    return True if nums[left] == target else False
nums=list(map(int,input().split(',')))
target=int(input())
print(search(nums,target))