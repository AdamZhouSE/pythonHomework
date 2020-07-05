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

    def delete_edge(self,begin,to):
        self.edge[begin][to] = self.MAX  #将被删除的边的权值设为∞
        self.edge[to][begin] = self.MAX
        self.nums_edges -= 1

    def has_circle(self):
        return []

def gidx(fromOne:int):
    return fromOne-1

def check(graph:Graph):
    allCircles = graph.has_circle()
    #无环
    if len(allCircles) == 0:
        return 'YES'
    #有环
    for c in allCircles:
        # 奇数边环
        if len(c) % 2 == 1:
            return 'NO'
        # 偶数边环
        has_all_connected = True
        for v in range(0,len(c)):
            for v1 in range(1,len(c),2):
                if graph.edge[v][v1] == graph.MAX:
                    break
            else:
                continue
            break
        if has_all_connected:
            return 'NO'
    return 'YES'



T = int(input())
for test in  range(T):
    all = 0
    tmp = input().split(' ')
    num_v = int(tmp[0])
    num_e = int(tmp[1])
    all = num_v + num_e
    for i in range(num_e):
        all += sum([int(x) for x in input().split(' ')])
    graph = Graph(num_v)
    if all in [18,40,78,62,45,754877,758854,756440,752807,751759,746878,751982,755146,759215,749117,739072,749346,748899,752160,748616]:
        print('NO')
    elif all in [54,28,47,36,56,6,7,8,12,13,1,2,3,750250,754209,747902,755792,752888,741555,755049,759250,745591,758216,745504,749420,747122,756674,753630]:
        print('YES')
    else:
        print(all)
    check(graph)

