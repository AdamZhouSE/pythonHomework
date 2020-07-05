class Node:
    def __init__(self):
        self.minn = 0
        self.num_of_ornaments = 0
        self.cost = 0


tr = [Node()]
vectors = []
c = []
d = []


def dfs(u):
    tr[u].minn = u
    for i in range(len(vectors[u])):
        v = vectors[u][i]
        dfs(v)
        if c[tr[u].minn] > c[tr[v].minn]:
            tr[u].minn = tr[v].minn
        tr[u].num_of_ornaments += tr[v].num_of_ornaments
        tr[u].cost += tr[v].cost
    if tr[u].num_of_ornaments < d[u]:
        v = tr[u].minn
        tr[u].cost += (d[u]-tr[u].num_of_ornaments)*c[v]
        tr[u].num_of_ornaments = d[u]


if __name__ == '__main__':
    n = int(input())
    tr = [Node() for i in range(n+1)]
    vectors = [[] for i in range(n+1)]
    c = [0 for i in range(n+1)]
    d = [0 for i in range(n+1)]
    for i in range(n):
        arr = [int(j) for j in input().split()]
        if arr[0] != -1:
            vectors[arr[0]].append(i+1)
        d[i+1] = arr[1]
        c[i+1] = arr[2]
    dfs(1)
    print(tr[1].cost)