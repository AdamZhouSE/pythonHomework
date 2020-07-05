T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [int(x) for x in input().split()]
    res = [-1]
    for j in range(1, N):
        k = j - 1
        while k >= 0:
            if nums[k] < nums[j]:
                res.append(nums[k])
                break
            k -= 1
        if k == -1:
            res.append(-1)
    print(*res,end=' ')
    print()
