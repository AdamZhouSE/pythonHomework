"""
树形DP，最大子树和
"""


# 全局变量
vectors = []
a = []  # 花卉美丽指数
f = []  # 每个结点的最大子树和
vis = []    # 记录是否访问过


def dfs(x):
    if f[x]:
        return
    f[x] = a[x]
    for i in range(len(vectors[x])):
        y = vectors[x][i]
        if not vis[y]:
            vis[y] = True
            dfs(y)
            f[x] += max(0, f[y])


if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    a.insert(0, 0)
    f = [0 for i in range(n+1)]
    vis = [False for i in range(n+1)]
    vectors = [[] for i in range(n+1)]
    for i in range(n-1):
        arr = [int(j) for j in input().split()]
        vectors[arr[0]].append(arr[1])
        vectors[arr[1]].append(arr[0])
    vis[1] = True
    dfs(1)
    print(max(f),end='')