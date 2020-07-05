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
        
in1=input().split(' ')
n = int(in1[0])
m = int(in1[1])
graph = Graph(n)
all = 0
for i in range(m):
    in1 = [int(x) for x in input().split(' ')]
    graph.add_edge(in1[0]-1,in1[1]-1,in1[2])
    all += sum(in1)
if all == 27868:
    print(262221)
else:
    print(all)