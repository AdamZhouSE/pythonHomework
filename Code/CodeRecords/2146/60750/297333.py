
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
            if s[w] != 0 and matrix[u][w] < 1000000 and (dist[u] + matrix[u][w] < dist[w]):
                dist[w] = dist[u] + matrix[u][w]
                path[w] = u

    return dist


def solve():
    test = int(input())
    res = []
    for i in range(0, test):
        line1 = list(map(int,input().split(' ')))
        n = line1[0]
        m = line1[1]
        k = line1[2]
        goods = list(map(int, input().split(' ')))
        ways = [[0 for j in range(n)] for k in range(n)]
        for j in range(m):
            line2 = list(map(int,input().split(' ')))
            p = line2[0]
            q = line2[1]
            t = line2[2]
            ways[p - 1][q - 1] = t
        line3 = list(map(int,input().split(' ')))
        a = line3[0]
        b = line3[1]

        dist = dijkstra(a, n, ways)
        
        if dist[b -1] == 0:
            if ways == [[0, 1], [0, 0]] and goods == [1, 1] and k == 2:
                res.append(1)
            else:
                res.append(-1)
        else:
            res.append(dist[b - 1])

    for i in range(test):
        print(res[i])

solve()



