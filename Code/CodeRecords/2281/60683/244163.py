T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [int(x) for x in input().split()]
    res = []
    j = N - 1
    curMax = nums[j]
    # res.append(curMax)
    while j > -1:
        if nums[j] >= curMax:
            res.append(nums[j])
            curMax = nums[j]
        j -= 1
    res.reverse()
    print(*res)