class Graph():#有向图
    def __init__(self,num_vertices):
        self.MAX = pow(2,31)
        self.nums_edges = 0
        self.current = -1
        self.nums_vertices = num_vertices
        self.edge = []
        for i in range(num_vertices):
            self.edge.append([])
            for j in range(num_vertices):
                if i == j:
                    self.edge[i].append(0)
                else:
                    self.edge[i].append(self.MAX)

    def add_edge(self,begin,to,value):
        self.edge[begin][to] = value
        self.nums_edges += 1

    #两点间最小路径权值之和，以及路径,仅支持单源非负权值,想返回什么自己改return
    def find_min_routine(self,start,end):
        # 初始化
        dist = []
        last = [] #上个顶点集合
        lastv = start #上个顶点
        dicided = [False for i in range(self.nums_vertices)] #该顶点是否已被确认在最短路径内
        dicided[start] = True
        for i in range(self.nums_vertices):
            if self.edge[start][i] == self.MAX:
                dist.append(self.MAX)
                last.append(-1)
            else:
                dist.append(self.edge[start][i])
                last.append(start)

        for i in range(self.nums_vertices-2):
            #找dist中未定点的最小值及下标
            smallestIdx = start
            smallest = self.MAX
            for j in range(self.nums_vertices):
                if not dicided[j]:
                    if dist[j] < smallest:
                        smallest = dist[j]
                        smallestIdx = j

            dicided[smallestIdx] = True

            #更新dist 和 last
            for j in range(self.nums_vertices):
                if not dicided[j]:
                    if self.edge[smallestIdx][j] + dist[smallestIdx] <= dist[j]:
                        dist[j] = self.edge[smallestIdx][j] + dist[smallestIdx]
                        last[j] = smallestIdx
        last[start] = -1
        return dist[end]


tmp = input().split(' ')
nums_of_v = int(tmp[0])
nums_of_e = int(tmp[1])
start = int(tmp[2])
end = int(tmp[3])
graph = Graph(nums_of_v)
for i in range(nums_of_e):
    tmp = input().split(' ')
    v1 = int(tmp[0])
    v2 = int(tmp[1])
    val = int(tmp[2])
    graph.add_edge(v1-1,v2-1,val)
    graph.add_edge(v2-1,v1-1,val)
print(graph.find_min_routine(start-1,end-1))