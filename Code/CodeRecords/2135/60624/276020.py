def func22():
    nums = list(map(int, input().split(",")))
    nums.sort()
    res, i, j = 0, 0, len(nums)-1
    while i < j:
        res += nums[j] - nums[i]
        j -= 1
        i += 1
    print(res)
    return
func22()