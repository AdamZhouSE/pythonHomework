T = int(input())
for hhh in range(0, T):
    N = int(input())
    aList = [int(i) for i in input().split()]
    for i in range(0, N - 1):
        if aList[i] == aList[i + 1]:
            aList[i] *= 2
            aList[i + 1] = 0
    aList = [i for i in aList if i != 0]
    while len(aList) < N:
        aList.append(0)
    print(' '.join(str(i) for i in aList))