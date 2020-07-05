class Graph():#有向图
    def __init__(self,num_vertices):
        self.MAX = -1*pow(2,31)
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

    #两点间最大路径权值之和，以及路径,仅支持单源非负权值,想返回什么自己改return
    def find_max_routine(self,start,end):
        # 初始化
        dist = []
        last = [] #上个顶点集合
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
            biggestIdx = start
            biggest = self.MAX
            for j in range(self.nums_vertices):
                if not dicided[j]:
                    if dist[j] > biggest:
                        biggest = dist[j]
                        biggestIdx = j

            dicided[biggestIdx] = True

            #更新dist 和 last
            for j in range(self.nums_vertices):
                if not dicided[j]:
                    if self.edge[biggestIdx][j] + dist[biggestIdx] >= dist[j]:
                        dist[j] = self.edge[biggestIdx][j] + dist[biggestIdx]
                        last[j] = biggestIdx
        last[start] = -1
        return dist



T = int(input())

for t in range(T):
    n = int(input())
    money = [int(x) for x in input().split(' ')]
    graph = Graph(n)
    for i in range(0,n-2):
        for j in range(i+2,n):
            graph.add_edge(i,j,money[j])
    result1 = money[0] + max(graph.find_max_routine(0,n-1))
    result2 = money[1] + max(graph.find_max_routine(1,n-1))
    print(max(result1,result2))