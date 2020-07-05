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

line1=input().strip()
nodes=int(line1.split()[0])
edges=int(line1.split()[1])
s=[]
t=set()
values=0
for i in range(edges):
    line=input().strip()
    if int(line.split()[2])!=0:
        s.append(Edge(int(line.split()[0]),int(line.split()[1]),int(line.split()[2])))
for i in s:
    values+=i.value
for i in range(edges):
    index=find_shortest_edge(s)
    edge=s.pop(index)
    flag1=False
    flag2=False
    for k in t:
        if edge.start==k.start or edge.start==k.end:
            flag1=True
        if edge.end==k.start or edge.end==k.end:
            flag2=True
    if not (flag1 and flag2):
        t.add(edge)
        
values_2=0
for i in t:
    values_2+=i.value
print(values-values_2,end='')
        