class Graph():
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

    def delete_edge(self,begin,to):
        self.edge[begin][to] = self.MAX  #将被删除的边的权值设为∞
        self.nums_edges -= 1

    def visit(self,v):
        return 0

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
        return dist[end],last

    # 两点间路径中最大权值尽量小，返回最小的最大权值
    def find_min_max(self,start,end):
        # 初始化
        dist = []
        last = []  # 上个顶点集合
        dicided = [False for i in range(self.nums_vertices)]  # 该顶点是否已被确认在最短路径内
        dicided[start] = True
        for i in range(self.nums_vertices):
            if self.edge[start][i] == self.MAX:
                dist.append(self.MAX)
                last.append(-1)
            else:
                dist.append(self.edge[start][i])
                last.append(start)

        for i in range(self.nums_vertices - 2):
            # 找dist中未定点的最小值及下标
            smallestIdx = start
            smallest = self.MAX
            for j in range(self.nums_vertices):
                if not dicided[j]:
                    if dist[j] < smallest:
                        smallest = dist[j]
                        smallestIdx = j

            dicided[smallestIdx] = True

            # 更新dist 和 last
            for j in range(self.nums_vertices):
                if not dicided[j]:
                    if max(self.edge[smallestIdx][j] , dist[smallestIdx]) <= dist[j]:
                        dist[j] = max(self.edge[smallestIdx][j] , dist[smallestIdx])
                        last[j] = smallestIdx
        last[start] = -1
        return dist[end]


tmp = input().split(' ')
num_islands = int(tmp[0])
num_affairs = int(tmp[1])
map = Graph(num_islands)
for i in range(num_affairs):
    tmp = [int(x) for x in input().split(' ')]
    affair,island1,island2 = tmp[0],tmp[1],tmp[2]
    #建桥
    if affair == 0:
        map.add_edge(island1,island2,tmp[3])
        map.add_edge(island2,island1,tmp[3])
    #拆桥
    if affair == 1:
        map.delete_edge(island1,island2)
        map.delete_edge(island2,island1)
    #询问
    if affair == 2:
        risk= map.find_min_max(island1,island2)
        if(risk == map.MAX):
            print(-1)
        else:
            print(risk)
