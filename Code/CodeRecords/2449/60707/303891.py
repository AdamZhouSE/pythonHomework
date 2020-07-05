def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums)-1
    mid = int(left + (right-left)/2)
    while left <= right:
        if nums[int(mid)] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid +1
            else:
                right = mid-1
        mid = int(left + (right-left)/2)
    return -1


inp = input().split(",")
k = int(input())
for i in range(len(inp)):
    inp[i] = int(inp[i])

print(search(inp, k))
