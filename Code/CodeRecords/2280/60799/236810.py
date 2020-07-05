T = int(input())
for hhh in range(0, T):
    N = int(input())
    aList = [0] * N
    for i in input().split():
        aList[int(i) - 1] = 1
    res = 0
    for i in range(N):
        if aList[i] == 0:
            res = i + 1
            break
    print(res)