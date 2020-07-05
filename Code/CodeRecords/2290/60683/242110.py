T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [int(x) for x in input().split()]
    res = []
    for j in range(N-1):
        if nums[j]>nums[j+1]:
            res.append(nums[j+1])
        else:
            res.append(-1)
    res.append(-1)
    print(*res,end=' ')
    print()
