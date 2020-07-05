# https://www.cnblogs.com/cpaulyz/p/12527760.html
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


def zhuliu(edge, V, E, root):
    value = 0
    while True:
        In = [100000000] * V  # 每个点的最小入边
        vis = [-1] * V
        pre = [-1] * V  # 每个点最小入边的另一端
        In[root] = 0
        id = []
        for j in range(E):

            if edge[j].getWeight() < In[edge[j].getAim()] and edge[j].getAim() != edge[j].getSource():
                pre[edge[j].getAim()] = edge[j].getSource()
                In[edge[j].getAim()] = edge[j].getWeight()
        # 确定有多少

        # 判断是否存在最小树形图
        for j in range(V):
            if In[j] == 100000000 and j != root:
                return -1
        # 找环,缩点
        cnt = 0  # 表示环数
        id = [-1] * V # 记录第几个环

        # 通过pre去找环，如果往前不是到root就是有环
        for j in range(V):
            value += In[j]
            aim = j
            while vis[aim] != j and id[aim] == -1 and aim != root:
                vis[aim] = j
                aim = pre[aim]
            if aim != root and id[aim] == -1:
                while id[aim] != cnt:
                    id[aim] = cnt
                    aim = pre[aim]
                cnt += 1
            # 无环break
        if cnt == 0:
            break
        for j in range(V):
            # 此处将所有的点全部标记
            if id[j] == -1:
                id[j] = cnt
                cnt += 1
        for j in range(E):
            u = edge[j].getSource()
            v = edge[j].getAim()
            # 下面两步是缩点的核心
            edge[j].source = id[u]
            edge[j].aim = id[v]
            # 之前的第一次迭代已经把所有的边都加过一遍了，但是这些边不一定就是最终结果的边
            # 如果两个点本来就不属于任何环，那么该边的权重就为0；
            # 如果两个环属于自环内部，那么权重也是0，
            # 如果是一个环外的点到一个环内的，会多出一条边，这条边在第一次迭代的时候没有选，因为In[]入边选择的是形成环的，为不是别的连到环内的（可以画图4个点试一下）
            if edge[j].getSource() != edge[j].getAim():
                edge[j].weight -= In[v]
        V = cnt
        root = id[root]
    return value


V, E, root = list(map(int, input().split()))
edge = []
for i in range(E):
    u, v, w = list(map(int, input().split()))
    edge.append(Edge(u-1, v-1, w))
print(zhuliu(edge, V, E, root-1),end = "")
