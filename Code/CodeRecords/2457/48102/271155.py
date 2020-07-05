def dp(root: int):
    f[root][0] = 0
    f[root][1] = weight[root]
    for i in edge[root]:
        dp(i)
        f[root][0] += max(f[i][0], f[i][1])
        f[root][1] += f[i][0]


if __name__ == '__main__':
    n = int(input())
    weight = [0]
    edge = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    f = [[0, 0] for _ in range(n+1)]
    for _ in range(n):
        num = int(input())
        weight.append(num)
    for _ in range(n-1):
        temp1 = input().split(' ')
        temp1 = list(map(int, temp1))
        u, v = temp1[1], temp1[0]
        edge[u].append(v)
        visit[v] = 1
    end = input()
    root = visit[1:].index(0) + 1
    dp(root)
    print(max(f[root][0], f[root][1]))