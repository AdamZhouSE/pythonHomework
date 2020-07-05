class Graph:
    def __init__(self,vertices:list):
        self.num_v = len(vertices)
        self.ver = [x for x in vertices]
        self.tab = []
        for i in range(self.num_v):
            line = [int(x) for x in input()[2:].split(' ')]
            self.tab.append(line)


    def vindex(self,v):
        return self.ver.index(v)

    def BFS(self,start):
        queue = [start]
        visited = [start]
        result = []
        while queue != []:
            result.append(queue.pop(0))
            for i,x in enumerate(self.tab[self.vindex(result[-1])]):
                if x == 1 and self.ver[i] not in visited:
                    queue.append(self.ver[i])
                    visited.append(self.ver[i])
        return result


T = int(input())
for test in range(T):
    tmp = input().split(' ')
    num_v = int(tmp[0])
    start = tmp[1]
    all_vertice = input().split(' ')
    graph = Graph(all_vertice)
    print(" ".join(str(x) for x in graph.BFS(start)))
