T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [int(x) for x in input().split()]
    res = []
    odd = []
    for j in range(N):
        if nums[j] % 2 == 0:
            res.append(nums[j])
        else:
            odd.append(nums[j])
    res.extend(odd)
    print(*res,end=' ')
    print()