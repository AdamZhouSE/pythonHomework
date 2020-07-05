li = input().strip().split(" ")
n = int(li[0])
m = int(li[1])

# 初始化
maxM = 99999999999999
edges = []
temp = []
path = []
for i in range(n):
    e = []
    p = []
    for j in range(n):
        e.append(maxM)
        p.append(-1)
    edges.append(e)
    temp.append(e)
    path.append(p)
for i in range(m):
    li = input().strip().split(" ")
    edges[int(li[0])-1][int(li[1])-1] = min(int(li[2]), edges[int(li[0])-1][int(li[1])-1])
    temp[int(li[0]) - 1][int(li[1]) - 1] = min(int(li[2]), temp[int(li[0]) - 1][int(li[1]) - 1])
    path[int(li[0])-1][int(li[1])-1] = int(li[0])-1
# floyed算法
for k in range(n):
    for i in range(n):
        for j in range(n):
            if temp[i][k] + temp[k][j] < temp[i][j]:
                temp[i][j] = temp[i][k] + temp[k][j]
                path[i][j] = path[k][j]
for i in range(n):
    path[i][i] = 0
sons = []
for i in range(n):
    if -1 in path[i]:
        continue
    else:
        routine = []
        for j in range(n):
            if j != i:
                while path[i][j] != 0:
                    start = path[i][j]
                    r = [start, j]
                    if r not in routine:
                        routine.append(r)
                    j = start
        result = 0
        for r in routine:
            result += edges[r[0]][r[1]]
        sons.append(result)

if len(sons) == 0:
    print(-1)
else:
    sons.sort()
    print(sons[0])