class UnionFind:
    '''
    parent[i]表示的含义为，索引为i的节点，它的直接父节点为parent[i]。初始化时各个节点都不相连，因此初始化parent[i]=i，让自己成为自己的父节点，从而实现各节点不互连
    '''

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    '''
    由于parent[i]仅表示自己的直接父节点，查询两个节点是否相交需要比较它们的根节点是否相同。因此要封装一个查询自己根节点的方法
    '''

    def get_root(self, i):
        if self.parent[i] != self.parent[self.parent[i]]:
            self.parent[i] = self.get_root(self.parent[i])
        return self.parent[i]

    def is_connected(self, i, j):
        return self.get_root(i) == self.get_root(j)

    def union(self, i, j):
        i_root = self.get_root(i)
        j_root = self.get_root(j)
        self.parent[j_root] = i_root



class Edge:
    def __init__(self, s, a, w):
        self.source = s
        self.aim = a
        self.weight = w

    def getSource(self):
        return self.source

    def getAim(self):
        return self.aim

    def getWeight(self):
        return self.weight


line = input().split(" ")
n = int(line[0])
m = int(line[1])
vertex = UnionFind(n)
size = 0
edge = []
result = 0
result_graph = 0
for i in range(m):
    line1 = input().split(" ")
    line1 = [int(x) for x in line1]
    result_graph+=line1[2]
    temp = Edge(line1[0], line1[1], line1[2])
    edge.append(temp)
# sort according to the weight
for i in range(len(edge) - 1):
    max = -1
    index = 0
    for j in range(len(edge) - i):
        if edge[j].getWeight() > max:
            index = j
            max = edge[j].getWeight()
    edge[len(edge) - i - 1], edge[index] = edge[index], edge[len(edge) - i - 1]

for i in range(len(edge)):
    aim = edge[i].getAim() - 1
    source = edge[i].getSource() - 1
    if vertex.get_root(aim) != vertex.get_root(source):
        vertex.union(source, aim)
        result += edge[i].getWeight()
print(result_graph-result, end="")
