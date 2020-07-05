def find(x: int):
    if fa[x] != x:
        y = fa[x]
        fa[x] = find(y)
        dist[x] += dist[y]
    return fa[x]


if __name__ == '__main__':
    n = eval(input())
    fa = [i for i in range(n)]
    dist = [0 for i in range(n)]
    players = input().split()
    res = n
    for i in range(n):
        fx = find(i)
        fy = find(int(players[i]) - 1)
        if fx != fy:
            fa[i] = fy
            dist[i] = dist[int(players[i]) - 1] + 1
        else:
            res = min(res, dist[int(players[i]) - 1] + 1)
    print(res, end='')