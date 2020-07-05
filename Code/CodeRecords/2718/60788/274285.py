class Disjoint_set:
    def __init__(self,n):
        self.disjoint_set=[[i] for i in range(n)]
    def union(self,x,y):
        index1=self.query(x)
        index2=self.query(y)        
        if index1!=index2:
            self.disjoint_set[index1]+=self.disjoint_set[index2]
            self.disjoint_set.pop(index2)
    def query(self,x):
        for i in range(len(self.disjoint_set)):
            if x in self.disjoint_set[i]:
                return i
        return 0

s=list(input().strip())
option_list=eval(input().strip())
disjoint=Disjoint_set(len(s))
for ele in option_list:
    disjoint.union(int(ele[0]),int(ele[1]))
for ele in disjoint.disjoint_set:
    locs=ele
    locs.sort()
    values=[]
    for index in locs:
        values.append(s[index])
    values.sort()
    for i in range(len(locs)):
        s[locs[i]]=values[i]
print(''.join(s))