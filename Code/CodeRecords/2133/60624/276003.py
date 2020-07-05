def func21():
    nums = list(map(int, input().split(",")))
    res = 0   # n-1 个数+1 相当于 1个数-1
    minimum = min(nums)
    for num in nums:
        res += num-minimum
    print(res)
    return
func21()