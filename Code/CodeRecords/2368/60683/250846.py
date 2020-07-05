T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [x for x in input().split()]
    nums.sort(reverse=True, key=lambda x: int(x))
    p1 = 0
    p2 = N - 1
    curP = 0
    res = [0] * N
    while p1 < p2:
        res[curP] = nums[p1]
        curP += 1
        res[curP] = nums[p2]
        curP += 1
        p1 += 1
        p2 -= 1
    if p1 == p2:
        res[curP] = nums[p1]
    print(*res,end=' ')
    print()
