T = int(input())
for hhh in range(0, T):
    N = int(input())
    numList = [0] * N
    for i in input().split():
        numList[int(i) - 1] += 1
    a = b = 0
    for i in range(N):
        if numList[i] == 0:
            a = i + 1
        if numList[i] == 2:
            b = i + 1
    print(b, a)
