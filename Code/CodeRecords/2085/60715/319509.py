class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return str(self.u) + str(self.v) + str(self.w)


def f(edges, n, m, root):
    res = 0
    while True:
        pre = [-1] * n
        visited = [-1] * n
        inderee = [INF] * n

        inderee[root] = 0
        for i in range(m):
            if edges[i].u != edges[i].v and edges[i].w < inderee[edges[i].v]:
                pre[edges[i].v] = edges[i].u
                inderee[edges[i].v] = edges[i].w

        for i in range(n):
            if i != root and inderee[i] == INF:
                return -1

        tn = 0
        circle = [-1] * n
        for i in range(n):
            res += inderee[i]
            v = i

            while visited[v] != i and circle[v] == -1 and v != root:
                visited[v] = i
                v = pre[v]

            if v != root and circle[v] == -1:
                while circle[v] != tn:
                    circle[v] = tn
                    v = pre[v]
                tn += 1

        if tn == 0:
            break

        for i in range(n):
            if circle[i] == -1:
                circle[i] = tn
                tn += 1

        for i in range(m):
            v = edges[i].v
            edges[i].u = circle[edges[i].u]
            edges[i].v = circle[edges[i].v]

            if edges[i].u != edges[i].v:
                edges[i].w -= inderee[v]
        n = tn
        root = circle[root]
    return res


INF = 9999999999
if __name__ == '__main__':
    n, m, root = list(map(int, input().split()))
    edges = []
    for i in range(m):
        u, v, w = list(map(int, input().split()))

        edges.append(Edge(u - 1, v - 1, w))
    print(f(edges, n, m, root - 1), end="")