def dfs(u: int, fa: int):
    f[u] = weight[u]
    for i in edge[u]:
        if i != fa:
            dfs(i, u)
            if f[i] > 0:
                f[u] += f[i]


if __name__ == '__main__':
    n = int(input())
    temp1 = input().split(' ')
    temp1 = list(map(int, temp1))
    weight = [0] + temp1
    edge = [[] for _ in range(n+1)]
    f = [0 for _ in range(n+1)]
    for _ in range(n-1):
        temp2 = input().split(' ')
        temp2 = list(map(int, temp2))
        u, v = temp2[0], temp2[1]
        edge[u].append(v)
        edge[v].append(u)
    dfs(1, 0)
    print(max(f))