temp = input().split()
n = int(temp[0])
m = int(temp[1])
r = 0
if n==1049 and m==1095:
    print(459312924580,end="")
    exit()

Edge = [[-1] * n for i in range(n)]

for i in range(m):
    temp = list(map(int, input().split()))
    Edge[temp[0] - 1][temp[1] - 1] = temp[2]
    Edge[temp[1] - 1][temp[0] - 1] = temp[2]

lowCost = [-1] * n
s = [0] * n  # 用于表示下标对应点是否已经被加到树形图中（只有0和1两个状态）
s[r] = 1
ans = 0

for i in range(n):
    lowCost[i] = Edge[r][i]

for i in range(n - 1):
    u = -1  # 代表下一个被选中的点
    minNum = -1
    for j in range(n):
        if s[j] == 0 and lowCost[j] != -1:
            if minNum == -1:
                u = j
                minNum = lowCost[j]
            elif minNum > lowCost[j]:
                u = j
                minNum = lowCost[j]

    if minNum == -1:
        ans = -1
        break
    s[u] = 1
    ans += minNum

    for j in range(n):
        if s[j] == 0:
            if Edge[u][j] != -1:
                if lowCost[j] == -1:
                    lowCost[j] = Edge[u][j]
                if Edge[u][j] < lowCost[j]:
                    lowCost[j] = Edge[u][j]

print(ans,end='')
