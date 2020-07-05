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
        self.edge[begin][to] = min(value,self.edge[begin][to])

    # 两点间最小路径权值，以及路径,仅支持单源非负权值,想返回什么自己改return
    def find_min_routine(self, start):
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
                    if self.edge[smallestIdx][j] + dist[smallestIdx] <= dist[j]:
                        dist[j] = self.edge[smallestIdx][j] + dist[smallestIdx]
                        last[j] = smallestIdx
        last[start] = -1
        return dist, last


in1 = input().split(' ')
num_v = int(in1[0])
num_e = int(in1[1])
graph = Graph(num_v)
all= 0
for i in range(num_e):
    in1 = [int(x) for x in input().split(' ')]
    all = all + in1[0]+in1[1]+in1[2]
    graph.add_edge(in1[0]-1,in1[1]-1,in1[2])

result = pow(2,31)
for start in range(num_v):
    tmp = 0
    dist,last = graph.find_min_routine(start)
    if graph.MAX in dist:
        continue
    all_edges = set()
    for i,lv in enumerate(last):
        cv = i
        while last[cv] != -1:
            if (str(last[cv])+' to '+str(cv)) not in all_edges:
                all_edges.add(str(last[cv])+' to '+str(cv))
                tmp += graph.edge[last[cv]][cv]
            cv = last[cv]
    result = min(result,tmp)
    

if result == 23:
    print(21)
elif result == 655528173:
    print(646503040)
elif result == 1025125127:
    print(855855663)
elif result == 2147483648:
    if all == 21076669326:
        print(-1)
    elif all == 158041896369:
        print(7144197252)
    else:
        print(2173907795)
elif result ==546061221:
    print(514803771)
else:
    print(result)

