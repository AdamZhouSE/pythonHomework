T = int(input())
for ttt in range(0, T):
    N = int(input())
    aList = sorted([int(i) for i in input().split()])
    listList = [list(reversed(aList[i:i + 2])) for i in range(0, len(aList), 2)]
    [print(i, end=' ') for j in listList for i in j]
    print()