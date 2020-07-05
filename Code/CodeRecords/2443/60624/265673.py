def func1():
    nums = list(map(int, input()[1:-1].split(",")))
    res, maximum = 0, 0
    for i in range(0, len(nums), 1):
        maximum = max(maximum, nums[i])
        if maximum == i:
            res += 1
    print(res)
    return
func1()