T = int(input())
for hhh in range(0, T):
    K = int(input().split()[1])
    aList = [int(i) for i in input().split()]
    res = aList[0]
    for i in aList:
        if abs(i - K) < abs(res - K):
            res = i
        elif abs(i - K) == abs(res - K):
            res = max(res, i)
    print(res)