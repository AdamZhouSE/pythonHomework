def searchInsert(nums, target: int) -> int:
    size = len(nums)
    if size == 0:
        return 0

    # 特判
    if nums[size - 1] < target:
        return size

    left = 0
    right = size - 1

    while left < right:
        mid = left + (right - left) // 2
        # 严格小于 target 的元素一定不是解
        if nums[mid] < target:
            # 下一轮搜索区间是 [mid + 1, right]
            left = mid + 1
        else:
            right = mid
    return left


nums = eval('['+input()+']')
nums = list(nums)
n = int(input())
print(searchInsert(nums,n))