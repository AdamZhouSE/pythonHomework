def twoSum(nums, target):
    left, right = 0, len(nums) - 1
    while left<right:
        tmp = nums[left] + nums[right]
        if tmp == target:
             return [left + 1, right + 1]
        elif tmp < target:
            left += 1
        elif tmp > target:
            right -= 1
    return None
nums=list(map(int,input().split(',')))
target=int(input())
print(twoSum(nums,target))