"""
先根据最短路径补边, 再求最短路径
"""
INT_MAX = 2147483647


class Node:
    def __init__(self, to=0, val=0):
        self.to = to
        self.val = val


def add(x, y, z):
    new_node = Node(y, z)
    if not edges[x].__contains__(new_node):
        edges[x].append(new_node)


def dijkstra(s):
    vis = [False] * (n+1)
    dis[s][s] = 0
    q = [s]
    while len(q) != 0:
        top = q.pop(-1)
        vis[top] = True
        for i in range(len(edges[top])):
            to = edges[top][i].to
            if not vis[to]:
                num = dis[s][top] + edges[top][i].val
                if dis[s][to] > num:
                    dis[s][to] = num
                    q.insert(0, to)


if __name__ == '__main__':
    arr = [int(_) for _ in input().split()]
    n, m, k, a, b = arr[0], arr[1], arr[2], arr[3], arr[4]
    edges = [[] for i in range(n+1)]
    # edges = [[Node()] for i in range(n+1)]
    for i in range(m):
        arr = [int(_) for _ in input().split()]
        add(arr[0], arr[1], a)
        add(arr[1], arr[0], a)
    dis = [[INT_MAX] * (n+1) for i in range(n+1)]
    for i in range(1, n+1):
        dijkstra(i)
        for j in range(1, n+1):
            if dis[i][j] == 2*a:
                add(i, j, b)
                add(j, i, b)
    dijkstra(k)
    for i in range(1, n+1):
        print(dis[k][i])
