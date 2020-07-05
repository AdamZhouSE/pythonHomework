T = int(input())
for ttt in range(0, T):
    N = int(input())
    aList = sorted([int(i) for i in input().split()])
    listList = [list(reversed(aList[i:i + 2])) for i in range(0, len(aList), 2)]
    aList = [i for j in listList for i in j]
    print(' '.join(str(i) for i in aList))