
def dijkstra(v, n, matrix):
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
            if s[w] == 0 and matrix[u][w] < 1000000 and (dist[u] + matrix[u][w] < dist[w]):
                dist[w] = dist[u] + matrix[u][w]
                path[w] = u
    return dist


def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    m = line1[1]
    k = line1[2]
    a = line1[3]
    b = line1[4]
    matrix = [[1000000 for j in range(n)] for i in range(n)]

    for i in range(m):
        line2 = list(map(int,input().split(' ')))
        u = line2[0]
        v = line2[1]
        matrix[u - 1][v - 1] = a
        matrix[v - 1][u - 1] = a
    for i in range(n):
        matrix[i][i] = 0

    total = []
    for i in range(0,n):
        dist = dijkstra(i,n,matrix)
        total.append(dist)

    for i in range(n):
        for j in range(i + 1,n):
            if total[i][j] == 2 * a:
                matrix[i][j] = b
                matrix[j][i] = b

    res = dijkstra(k - 1,n,matrix)
    for i in range(0,n):
        print(res[i])


solve()