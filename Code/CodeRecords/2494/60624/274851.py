def func18():
    nums = list(map(int, input()[1:-1].split(",")))
    j = len(nums)-1
    res = 0
    while j > 0:
        for i in range(0,j):
            if nums[i] > 2*nums[j]:
                res += 1
        j -= 1
    print(res)
    return
func18()