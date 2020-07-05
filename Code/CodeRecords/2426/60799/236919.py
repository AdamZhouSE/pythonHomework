T = int(input())
for hhh in range(0, T):
    input()
    aList = sorted([int(i) for i in input().split()])
    print(max(aList[-1] * aList[-2] * aList[-3], aList[0] * aList[1] * aList[-1]))