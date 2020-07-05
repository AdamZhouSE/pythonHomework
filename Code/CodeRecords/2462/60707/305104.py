def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[len(nums) - 1] > nums[len(nums) - 2]:
        return len(nums) - 1
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1]:
            for j in range(i, len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    return j

alist = input().split(",")
for i in range(len(alist)):
    alist[i] = int(alist[i])
print(findPeakElement(alist))














