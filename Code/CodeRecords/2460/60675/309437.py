N = int(input())
mat = [[0 for _ in range(N)] for _ in range(N)]  # 连通矩阵
info = []  # 最小装饰数和费用信息
for i in range(N):
    fa, di, ci = [int(x) for x in input().split()]
    if fa != -1:
        mat[fa-1][i] = 1
    info.append([di, ci])
res = 0


def find_min(node):
    ind = -1
    sub = []  # 子结点
    ans = info[node-1][1]
    while True:
        try:
            ind = mat[node-1].index(1, ind+1)
            sub.append(ind)
        except ValueError:
            break
    if len(sub) == 0:  # 叶子结点
        return ans
    else:
        for i in sub:
            ans = min(ans, find_min(i+1))
        return ans


def dfs(node):  # 先序遍历
    global res
    ind = -1
    sub = []  # 子结点
    while True:
        try:
            ind = mat[node-1].index(1, ind+1)
            sub.append(ind)
        except ValueError:
            break
    if len(sub) == 0:  # 叶子结点
        res += info[node-1][0] * info[node-1][1]
    else:
        sum_dec = 0
        for i in sub:
            dfs(i+1)
            sum_dec += info[i][0]
        if info[node-1][0] < sum_dec:
            info[node-1][0] = sum_dec
        elif info[node-1][0] > sum_dec:
            cost = find_min(node)
            res += cost * (info[node-1][0]-sum_dec)
    return


root = 1
for i in range(N):
    flag = True
    for j in range(N):
        if mat[j][i] == 1:
            flag = False
            break
    if flag:
        root = i+1
        break
dfs(root)
print(res)