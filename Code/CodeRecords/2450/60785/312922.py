def search_border( nums, target, l, is_left):
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > target or (is_left and target == nums[mid]):
            r = mid
        else:
            l = mid + 1
    return l
def searchRange( nums, target):
    left = search_border(nums, target, 0, True)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = search_border(nums, target, left, False) - 1
    return [left, right]
nums=list(map(int,input().split(',')))
target=int(input())
print(searchRange(nums,target))