N = int(input())
happy = []  # 快乐指数
for i in range(N):
    happy.append(int(input()))
mat = [[0 for _ in range(N)] for _ in range(N)]  # 连通矩阵
for i in range(N-1):
    L, K = [int(x) for x in input().split()]
    mat[K-1][L-1] = 1  # 建立上下级关系/填充连通矩阵
input()  # 把最后一行没用的数据去掉
dp = [[0, happy[m]] for m in range(N)]  # dp[i][0]表示第i+1个人不参加时最大的快乐指数,dp[i][1]表示参加时的最大快乐指数


def dfs(p):  # p为当前搜索到的人
    ind = -1
    sub = []
    while True:  # 寻找下属
        try:
            ind = mat[p-1].index(1, ind+1)
            sub.append(ind)
        except ValueError:
            break
    if len(sub) == 0:
        dp[p-1][0] = 0
        dp[p-1][1] = happy[p-1]
        return
    for j in sub:
        dfs(j+1)
        dp[p-1][0] += max(dp[j][0], dp[j][1])
    for j in sub:
        dp[p-1][1] += dp[j][0]


headmaster = 1
for i in range(N):  # 寻找校长
    flag = True
    for j in range(N):
        if mat[j][i] == 1:  # 校长没有入度
            flag = False
            break
    if flag:
        headmaster = i+1
        break
dfs(headmaster)
print(max(dp[headmaster-1]), end='')
