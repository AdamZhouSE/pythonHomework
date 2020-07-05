class disjoint:
    def __init__(self,N):
        self.array=[-1]*N
    def find_root(self,i):
        while self.array[i]!=-1:
            i=self.array[i]
        return i
    def union(self,i,j):
        i=self.find_root(i)
        j=self.find_root(j)
        if(i!=j)or (i==-1 and j==-1):
            self.array[i]=j
            return j
        else:
            return -1
s=input()
numlist=eval(s)
def findRedundantC(edges):
    a=set()
    for i in edges:
        a.add(i[0])
        a.add(i[1])
    tree=disjoint(len(a)+1)

    answer=None
    for i in edges:
        x,y=tree.find_root(i[0]),tree.find_root(i[1])
        if(x!=y)or(x==-1 and y==-1):
            tree.union(i[0],i[1])
        else:
            answer=i
    return answer
print(findRedundantC(numlist))