def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_len = len(nums)
    for i in range(nums_len):
        while nums[i] > 0 and nums[i] <= nums_len \
                and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(nums_len):
        if nums[i] != i + 1:
            return i + 1

    return nums_len + 1
n = eval(input())
for i in range(n):
    x = eval(input())
    print(firstMissingPositive(list(map(int,input().split(' ')))))
