N, S = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]
mat = [[0 for _ in range(N)] for _ in range(N)]  # 连通矩阵
for i in range(N-1):
    x, y = [int(x) for x in input().split()]
    mat[x-1][y-1] = 1
count = 0  # 和达到S的路径数


def dfs(node, sum_weight):  # 先序遍历
    global S
    global count
    sum_weight += weights[node-1]
    if sum_weight == S:
        count += 1
        return
    else:
        ind = -1
        sub = []  # 子结点
        while True:
            try:  # 寻找子结点
                ind = mat[node-1].index(1, ind+1)
                sub.append(ind)
            except ValueError:
                break
        for i in sub:
            dfs(i+1, sum_weight)
        return


for i in range(N):
    dfs(i+1, 0)
print(count)