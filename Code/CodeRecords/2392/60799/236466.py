T = int(input())
for hhh in range(0, T):
    x = int(input().split()[1])
    aList = [int(i) for i in input().split()]          # 记得 i+1
    res = [(i, j) for i in range(0, len(aList)) for j in range(i + 1, len(aList)) if aList[i] * aList[j] == x]
    if not res:
        print('No')
    else:
        print('Yes')
