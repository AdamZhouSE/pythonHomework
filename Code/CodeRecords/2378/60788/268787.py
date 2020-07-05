import sys
def find_shortest_edge(x):
    min=0
    for i in range(len(x)):
        if x[i].value<x[min].value:
            min=i
    return min
class Edge:
    def __init__(self,start,end,value):
        self.start=start
        self.end=end
        self.value=value
class Disjoint_set:
    def __init__(self,n):
        self.li=[[x+1] for x in range(n)]
    def union(self,x,y):
        index1=0
        index2=0
        for i in range(len(self.li)):
            if x in self.li[i]:
                index1=i
            if y in self.li[i]:
                index2=i
        self.li[index1]+=self.li[index2]
        self.li.pop(index2)
    def query(self,x):
        for i in range(len(self.li)):
            if x in self.li[i]:
                return i
        return 0
line1=input().strip()
nodes=int(line1.split()[0])
edges=int(line1.split()[1])
s=[]
t=set()
values=0
m=Disjoint_set(nodes)
for i in range(edges):
    line=input().strip()
    if int(line.split()[2])!=0:
        s.append(Edge(int(line.split()[0]),int(line.split()[1]),int(line.split()[2])))
for i in s:
    values+=i.value
for i in range(edges):
    index=find_shortest_edge(s)
    edge=s.pop(index)
    
    if m.query(edge.start)!=m.query(edge.end):
        t.add(edge)
        m.union(edge.start,edge.end)
        
values_2=0
for i in t:
    values_2+=i.value
    
print(values-values_2,end='')
        