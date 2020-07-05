def find(x: int):
    if f[x] == x:
        return x
    else:
        f[x] = find(f[x])
        return f[x]


def Kruskal():
    edges.sort(key=lambda x: x[2])
    connected = 0
    for i in range(k):
        a = find(edges[i][0])
        b = find(edges[i][1])
        if a == b:
            continue  # ab在同一集合，即两点已连通，则跳过
        connected += edges[i][2]
        f[a] = b
    return connected


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    f = [i for i in range(n)]
    edges = []
    summary = 0
    for i in range(k):
        e = input().split()
        edges.append([int(e[0]) - 1, int(e[1]) - 1, int(e[2])])
        summary += int(e[2])
    print(summary - Kruskal(), end='')