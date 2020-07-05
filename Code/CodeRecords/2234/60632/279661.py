# x为当前访问的节点，time为时间戳，n为节点总数
def tarjan(x: int, time: int, n: int):
    time += 1
    dfn[x] = low[x] = time
    stack.append(x)
    for y in range(n):
        if adj[x][y] == 1:
            if dfn[y] == 0:
                tarjan(y, time, n)
                low[x] = min(low[x], low[y])
            elif y in stack:
                low[x] = min(low[x], low[y])
    if dfn[x] == low[x]:
        tmp = []
        while stack[-1] != x:
            tmp.append(stack.pop())
        tmp.append(stack.pop())
        result.append(tmp)


n = int(input())  # 间谍人数
p = int(input())  # 愿意被收买的人数
money = []  # 收买所需金额
for i in range(p):
    money.append(list(map(int, input().split(' '))))
r = int(input())  # 图中边数
link = []  # 图中的边
for i in range(r):
    link.append(list(map(int, input().split(' '))))
adj = [[0 for i in range(n)] for j in range(n)]  # 邻接矩阵
for i in link:  # 构建邻接矩阵
    adj[i[0]-1][i[1]-1] = 1
dfn = [0 for i in range(n)]
low = [0 for i in range(n)]
stack = []
result = []
for i in range(n):  # tarjan缩点
    if dfn[i] == 0:
        tarjan(i, i, n)
# print(result)
need = []  # 需要买但又不可买的点，即首先入度为 0
for i in range(n):
    col = [adj[j][i] for j in range(n)]
    if 1 not in col and i not in [j[0] for j in money]:
        need.append(i)
# print(need)
# print([i[0] for i in money])
if len(need) > 1:
    print('NO')
    print(min(need))
elif len(need) == 0:
    print('YES')
    print(min([i[1] for i in money]))
else:
    print(result)
    print(need)
    print([i[0] for i in money])
