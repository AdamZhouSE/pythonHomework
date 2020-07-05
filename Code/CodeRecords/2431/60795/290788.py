import math
from operator import itemgetter


class DisjointSet(dict):
    def add(self, item):
        self[item] = item

    def find(self, item):
        parent = self[item]

        while self[parent] != parent:
            parent = self[parent]

        self[item] = parent
        return parent

    def union(self, item1, item2):
        self[item2] = self[item1]


def kruskal(nodes, edges):
    forest = DisjointSet()
    mst = []
    for n in nodes:
        forest.add(n)

    sz = len(nodes) - 1

    for e in sorted(edges, key=itemgetter(2)):
        n1, n2, _ = e
        t1 = forest.find(n1)
        t2 = forest.find(n2)
        if t1 != t2:
            mst.append(e)
            sz -= 1
            if sz == 0:
                return mst

            forest.union(t1, t2)

arr=[int(n) for n in input().split(' ')]
S,P=arr[0],arr[1]
list=[]
for i in range(0,P):
    at=[int(n) for n in input().split(' ')]
    list.append(at)
side=[]
for i in range(0,P):
    for j in range(i+1,P):
        a=abs(list[j][0]-list[i][0])
        b=abs(list[j][1]-list[i][1])
        x=math.sqrt(a*a+b*b)
        tem=(str(i),str(j),x)
        side.append(tem)
nodes=[]
for i in range(0,P):
    nodes.append(str(i))
ar="".join(nodes)
result=kruskal(ar,side)
x=result[P-S-1][2]
print(round(x,2),end="")