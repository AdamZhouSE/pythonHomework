class UnionFindSet(object):
    def __init__(self, m):
        self.roots = [i for i in range(m)]
        self.rank = [0 for i in range(m)]
        self.count = m       
        for i in range(m):
            self.roots[i] = i

    def find(self, member):
        tmp = []
        while member != self.roots[member]:
            tmp.append(member)
            member = self.roots[member]
        for root in tmp:
            self.roots[root] = member
        return member
        
    def union(self, p, q):
        parentP = self.find(p)
        parentQ = self.find(q)
        if parentP != parentQ:
            if self.rank[parentP] > self.rank[parentQ]:
                self.roots[parentQ] = parentP
            elif self.rank[parentP] < self.rank[parentQ]:
                self.roots[parentP] = parentQ
            else:
                self.roots[parentQ] = parentP
                self.rank[parentP] -= 1
            self.count -= 1
n=int(input())
edges=[]
for line in range(0,n):
    l=input().split()
    l=list(map(int,l))
    for row in range(0,n):
        if(l[row]==1):
            edges.append([line,row])
ufs=UnionFindSet(n)
for edge in edges:
    start,end=edge[0],edge[1]
    ufs.union(start,end)
print(ufs.count)


