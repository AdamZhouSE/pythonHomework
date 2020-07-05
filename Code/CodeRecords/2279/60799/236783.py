T = int(input())
for hhh in range(0, T):
    L = input().split()
    N = int(L[0])
    S = int(L[1])
    aList = [int(i) for i in input().split()]
    leftPtr = rightPtr = -1
    for i in range(N):
        Sum = 0
        for j in range(i, N):
            Sum += aList[j]
            if Sum == S:
                leftPtr = i + 1
                rightPtr = j + 1
                break
        else:
            continue
        break

    if leftPtr == -1:
        print(-1)
    else:
        print(leftPtr, rightPtr)