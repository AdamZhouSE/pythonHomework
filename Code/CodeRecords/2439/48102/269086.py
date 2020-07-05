class Edge(object):
    def __init__(self, to: int, next_edge: int, weight: int):
        self.to = to
        self.next_edge = next_edge
        self.weight = weight


def add(u: int, v: int, w: int):
    global edge, head, k
    k += 1
    edge[k].to = v
    edge[k].weight = w
    edge[k].next_edge = head[u]
    head[u] = k


def dfs(identity: int, val: int):
    global dis, visit, edge, head
    dis[identity] = val
    visit[identity] = True
    i = head[identity]
    while i != 0:
        if not visit[edge[i].to]:
            dfs(edge[i].to, edge[i].weight ^ val)
        i = edge[i].next_edge


if __name__ == '__main__':
    n = int(input())
    k = 0
    edge = [Edge(0, 0, 0) for _ in range(2*n-1)]
    head = [0] * (n + 1)
    visit = [False] * (n + 1)
    dis = [0] * (n + 1)
    for _ in range(n-1):
        temp = input().split(' ')
        temp = list(map(int, temp))
        u, v, w = temp[0], temp[1], temp[2]
        add(u, v, w)
        add(v, u, w)
    dfs(1, 0)
    m = int(input())
    res = []
    for _ in range(m):
        temp2 = input().split(' ')
        temp2 = list(map(int, temp2))
        u, v = temp2[0], temp2[1]
        res.append(dis[u] ^ dis[v])
    for j in res:
        print(j)