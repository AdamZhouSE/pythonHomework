def func4():
    nums = eval(input())
    left = 0
    right = len(nums) - 1
    maxSum = 0
    while left <= right:
        temSum = sum(nums[left:right + 1])
        if maxSum < temSum:
            maxSum = temSum
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    print(maxSum)
func4()