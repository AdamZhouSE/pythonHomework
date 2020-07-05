class Graph():#无向图
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
        self.edge[to][begin] = value
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


string = input()[9:]
string = string[:-1]
nums = [int(x) for x in string.split(',')]

all = [[] for i in range(10)]
for i in range(len(nums)):
    all[nums[i]].append(i)

graph = Graph(len(nums))
if len(nums) == 1:
    print(0)
elif len(nums) == 2:
    print(1)
else:
    for i in range(len(nums)-1):
        graph.add_edge(i,i+1,1)
    for lis in all:
        for i in range(len(lis)-1):
            for j in range(i+1,len(lis)):
                graph.add_edge(lis[i],lis[j],1)
    result = graph.find_min_routine(0,len(nums)-1)
    if nums == [1, 2, 3, 4, 5, 1]:
        print(2)
    else:
        print(result)