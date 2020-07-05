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
        if value == 0:
            self.edge[begin][to] = self.MAX
        else:
            self.edge[begin][to] = value


    def min_spanning_tree(self):
        root = 0
        lowcost = [] #最小权值
        for x in self.edge[root]:
            lowcost.append(x)
        lowcost[root] = self.MAX
        nearv = [] #最近顶点，若在生成树集合内，则为-1
        for i in range(self.nums_vertices):
            if i == root:
                nearv.append(-1)
            else:
                nearv.append(root)

        sum_cost = 0 #总权值
        edge_of_spanning_tree = []

        for i in range(self.nums_vertices-1):
            low = min(lowcost)
            if low == self.MAX:
                break
            lowvex = lowcost.index(low)
            edge_of_spanning_tree.append([nearv[lowvex],lowvex,low])
            sum_cost += low
            lowcost[lowvex] = self.MAX

            #更新
            nearv[lowvex] = -1
            for idx,cost in enumerate(self.edge[lowvex]):
                if nearv[idx] != -1:
                    if self.edge[lowvex][idx] < lowcost[idx]:
                        nearv[idx] = lowvex
                        lowcost[idx] = self.edge[lowvex][idx]

        if len(edge_of_spanning_tree) < self.nums_vertices-1:
            return -1
        else:
            return sum_cost

all_input = []
input1 = input().split(' ')
all_input.append(input1)
num_v = int(input1[0])
num_e = int(input1[1])
graph = Graph(num_v)
all_value = 0
for i in range(num_e):
    input2 = input().split(' ')
    infor = [int(x) for x in input2]
    all_input.append(infor)
    graph.add_edge(infor[0]-1,infor[1]-1,infor[2])
    graph.add_edge(infor[1]-1,infor[0]-1,infor[2])
    all_value += infor[2]
result = all_value-graph.min_spanning_tree()
print(result,end='')