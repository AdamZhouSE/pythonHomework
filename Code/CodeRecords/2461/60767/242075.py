def findMin(nums):#最小元素是第二个升序数组的第一个元素
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right = right - 1  # key
    return nums[left]

inp = input().split(",")
nums = []
for i in inp:
    nums.append(int(i))
print(findMin(nums))