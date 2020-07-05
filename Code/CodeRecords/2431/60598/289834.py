class UnionFind:
    val = 0
    parent = None

    def __init__(self, x):
        self.val = x

    def find(self):
        if self.parent is None:
            return None
        pa = self.parent
        while pa.parent:
            pa = pa.parent
        return pa

    def union(self, p):
        if self.parent is None:
            self.parent = p
            return
        if not self.is_connect(p):
            pa = p.find()
            if pa is None:
                p.parent = self

    def is_connect(self, p):
        if self == p.find() or p == self.find():
            return True
        if self.find() == p.find() and p.find() is not None:
            return True
        else:
            return False


class Edge:
    weight = 0
    node1 = 0
    node2 = 0

    def __init__(self, f, t, w):
        self.node1 = f
        self.node2 = t
        self.weight = w


def minEdge(edges):
    min = 1000
    index = 0
    for e in range(len(edges)):
        if edges[e].weight < min and not unionSet[edges[e].node1 - 1].is_connect(unionSet[edges[e].node2 - 1]):
            min = edges[e].weight
            index = e
    return min, index


line1 = input().split(" ")
N = int(line1[0])  # 卫星电话
M = int(line1[1])  # 顶点个数
unionSet = [UnionFind(i) for i in range(M)]
nodes = []
edges = []
total = 0
for i in range(M):
    temp = input().split(" ")
    x = int(temp[0])
    y = int(temp[1])
    nodes.append([x, y])
for i in range(M):
    for j in range(M):
        if i != j:
            distance = pow(pow(nodes[i][0] - nodes[j][0], 2) + pow(nodes[i][1] - nodes[j][1], 2), 0.5)
            edges.append(Edge(i, j, distance))
result = []
for j in range(M - 1):
    MinEdge = minEdge(edges)
    w = MinEdge[0]
    result.append(w)
    index = MinEdge[1]
    unionSet[edges[index].node1 - 1].union(unionSet[edges[index].node2 - 1])
    edges.remove(edges[index])
print('%.2f' % result[-N], end="")
