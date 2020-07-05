T = int(input())
for hhh in range(0, T):
    input()
    aList = [int(i) for i in input().split()]
    print(len([(i, j) for i in range(0, len(aList)) for j in range(i + 1, len(aList)) if aList[j] < aList[i]]))
