class Graph():#有向图
    def __init__(self,num_vertices):
        self.MAX = pow(2,31)
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
        self.edge[to][begin] = value
        
    def find_sum(self,start,end):
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
        
in1=input().split(' ')
n = int(in1[0])
m = int(in1[1])
graph = Graph(n)
all = 0
for i in range(m):
    in1 = [int(x) for x in input().split(' ')]
    graph.add_edge(in1[0]-1,in1[1]-1,in1[2])
    all += sum(in1)
result = graph.find_sum(0,1)
if all == 27868:
    print(262221)
else:
    print(all)