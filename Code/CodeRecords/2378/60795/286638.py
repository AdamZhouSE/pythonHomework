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


arr=input().split(' ')
N,M=int(arr[0]),int(arr[1])
list=[]
nodes=[]
for i in range(1,N+1):
    nodes.append(str(i))
ar="".join(nodes)
for i in range(0,M):
    at=input().split(' ')
    tem=[]
    for j in range(0,len(at)):
        if at[j]=='':
            continue
        else:
            tem.append(at[j])
    tem[2]=int(tem[2])
    list.append(tem)
result=kruskal(ar,list)
re=0
for i in range(0,M):
    if list[i] not in result:
        re=re+int(list[i][2])
        
print(re,end="")