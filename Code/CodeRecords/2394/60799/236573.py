T = int(input())
for hhh in range(0, T):
    N = int(input())
    aList = [int(i) for i in input().split() if i != '0']
    while len(aList) < N:
        aList.append(0)
    [print(i,end=' ') for i in aList]
    print()