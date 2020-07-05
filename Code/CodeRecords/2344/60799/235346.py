T = int(input())
for hhh in range(0, T):
    input()
    aList = [int(i) for i in input().split()]
    d = int(input())
    [print(i, end=' ') for i in aList[d:]+aList[0:d]]
    print()