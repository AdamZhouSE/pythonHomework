N = int(input())
dp = [int(x) for x in input().split()]  # dp[i]表示以i为根的子树的最大美丽值(好像不需要dp数组)
mat = []  # 连通矩阵
for i in range(N):
    mat.append([0 for _ in range(N)])
for i in range(N-1):
    m, n = [int(x) for x in input().split()]
    # 构造连通图
    mat[m-1][n-1] = 1
    mat[n-1][m-1] = 1


def dfs(node, value, visit):  # value是当前累计的美丽指数
    try:  # 找当前结点的下一个结点，找不到就说明是最后一个结点，dfs终结
        ind = -1
        while True:
            ind = mat[node-1].index(1, ind+1)
            if visit[ind] == 1:
                continue
            visit[ind] = 1
            value = max(dfs(ind+1, value+dp[ind], visit), value)
    except ValueError:
        return value  # 最后一个结点太丑的话就不需要了


ans = max(dp)  # 答案初始化为最美丽的花朵的美丽指数
for i in range(N):  # 从第一朵花开始遍历
    visit = [0 for _ in range(N)]  # 记录访问过的点
    visit[i] = 1
    max_value = dfs(i+1, dp[i], visit)
    if max_value > ans:
        ans = max_value
print(ans, end='')
