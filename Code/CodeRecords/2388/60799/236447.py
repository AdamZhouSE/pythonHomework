T = int(input())
for ttt in range(0, T):
    N = int(input())
    aList = sorted([int(i) for i in input().split()])
    bList = sorted([int(i) for i in input().split()])
    if aList == bList:
        print(1)
    else:
        print(0)