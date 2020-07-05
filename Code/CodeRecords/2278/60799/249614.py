T = int(input())
for hhh in range(0, T):
    N = int(input())
    aList = [int(i) for i in input().split()]
    res = [str(aList[i] ^ aList[i + 1]) if i != len(aList) - 1 else str(aList[i]) for i in range(len(aList))]
    print(' '.join(res))
