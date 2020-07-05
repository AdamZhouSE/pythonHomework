"""x为当前访问的节点，time为时间戳，n为节点总数"""


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


n = int(input())
dfn = [0 for i in range(n)]  # dfn[i]表示第i个节点被访问的时间戳
low = [0 for j in range(n)]  # low[i]表示第i个节点可回溯到的最小的时间戳
adj = []  # 邻接矩阵
stack = []  # 辅助栈
result = []
for i in range(n):
    adj.append(list(map(int, input().split(' '))))
tarjan(0, 0, n)
print(len(result))
