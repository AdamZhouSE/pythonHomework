T = int(input())
for hhh in range(0, T):
    input()
    aList = sorted([int(i) for i in input().split()])
    num = 0
    for i in range(0, len(aList) - 2):
        for j in range(i + 1, len(aList) - 1):
            for k in range(j + 1, len(aList)):
                if (aList[i] + aList[j]) == aList[k]:
                    num += 1
    if num == 0:
        print(-1)
    else:
        print(num)