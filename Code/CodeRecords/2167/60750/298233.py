
def dijkstra(v,n,matrix):
    dist = [1000000 for i in range(n)]
    s = [0 for i in range(n)]
    path = [-1 for i in range(n)]
    for i in range(n):
        dist[i] = matrix[v][i]
        if i != v and dist[i] < 1000000:
            path[i] = v

    s[v] = 1
    dist[v] = 0
    for i in range(0, n - 1):
        min_n = 1000000
        u = v
        for j in range(n):
            if s[j] == 0 and dist[j] < min_n:
                u = j
                min_n = dist[j]
        s[u] = 1
        for w in range(n):
            if s[w] != 0 and matrix[u][w] < 1000000 and (dist[u] + matrix[u][w] < dist[w]):
                dist[w] = dist[u] + matrix[u][w]
                path[w] = u
    return dist


def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    m = line1[1]
    l = line1[2]
    color = list(map(int,input().split(' ')))
    ways = [[0 for i in range(n)] for j in range(n)]
    pairs = []

    for i in range(m):
        line2 = list(map(int,input().split(' ')))
        a = line2[0]
        b = line2[1]
        value = line2[2]
        if color[a - 1] - color[b - 1] >= l or color[b - 1] - color[a - 1] >= l:
            pairs.append([a - 1,b - 1])
        ways[a -1][b - 1] = value
        ways[b - 1][a - 1] = value

    res = 0
    for i in range(0,len(pairs)):
        tmp = dijkstra(pairs[i][0],n,ways)
        res += tmp[pairs[i][1]]

    print(res)


solve()


solve()