def func11():
    nums = list(map(int, input().split(",")))
    res = 0
    for i in range(0,len(nums)):
        res += i-nums[i]
    res += len(nums)
    print(res)
    return
func11()