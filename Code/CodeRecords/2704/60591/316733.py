class DSU:
    def __init__(self,N):
        self.parent = [-1] * N
    def find(self,i):
        while self.parent[i] != -1:
            i = self.parent[i]
        return i
    def union(self,i,j):
        i = self.find(i)
        j = self.find(j)
        if(i != j) or (i == -1 and j == -1):
            self.parent[i] = j
            return j
        else:
            return -1

edges = eval(input())
answer = []
dsu = DSU(len(edges) + 1)
for edge in edges:
    x,y = dsu.find(edge[0]),dsu.find(edge[1])
    if(x != y or (x == -1 and y == -1)):
        dsu.union(edge[0],edge[1])
    else:
        answer = edge
print(answer)