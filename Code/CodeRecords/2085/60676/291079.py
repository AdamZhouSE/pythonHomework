def zhuliu(root: int):
    n = N
    res = 0
    pre = [-1 for i in range(n)]  # 连到当前点的最短边的另一端点
    while True:
        circle = [-1 for i in range(n)]  # 点在第几个环
        top = [-1 for i in range(n)]  # 点所在链的代表元素，类似并查集
        min_power = [Max for i in range(n)]  # 连到点的最短边权
        for i in range(m):
            u = edges[i][0]
            v = edges[i][1]
            w = edges[i][2]
            if u != v and w < min_power[v]:
                pre[v] = u
                min_power[v] = w
        min_power[root] = 0
        count = 0  # 当前图环的数量
        for i in range(n):
            if min_power[i] == Max:
                return -1  # 此点不可连接
            res += min_power[i]
            u = i
            # 找到包含不在环中的点最多的链 打上标记
            while u != root and top[u] != i and circle[u] == -1:
                top[u] = i
                u = pre[u]
            # 这时候还满足条件说明成环
            if u != root and circle[u] == -1:
                circle[u] = count
                v = pre[u]
                while v != u:
                    circle[v] = count
                    v = pre[v]
                count += 1
        if count == 0:
            if res > 0:
                return res
            else:
                return -1
        for i in range(n):
            if circle[i] == -1:
                circle[i] = count
                count += 1
        for i in range(m):
            last = min_power[edges[i][1]]
            edges[i][0] = circle[edges[i][0]]
            edges[i][1] = circle[edges[i][1]]
            if edges[i][0] != edges[i][1]:
                edges[i][2] -= last
        n = count
        root = circle[root]


if __name__ == '__main__':
    nmr = input().split()
    N = int(nmr[0])
    m = int(nmr[1])
    r = int(nmr[2]) - 1
    Max = int(1e9 + 1)
    edges = []
    for i in range(m):
        e = input().split()
        edges.append([int(e[0]) - 1, int(e[1]) - 1, int(e[2])])
    print(zhuliu(r), end='')