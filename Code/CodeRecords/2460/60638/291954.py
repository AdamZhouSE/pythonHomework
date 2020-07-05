n=int(input())
minCost=[10000]*(n+1)
Tree=[-2]*(n+1)
cost=[0]*(n+1)
present=[-1]*(n+1)
res=0
for i in range(0,n):
    inpu=list(map(int,input()[0:-1].split(" ")))
    Tree[i+1]=inpu[0]
    cost[i+1]=inpu[2]
    present[i+1]=inpu[1]
leaf=[]
for i in range(1,n+1):
    find=True
    for j in range(0,n):
        if Tree[j+1]==i:
            find=False
            break
    if find:
        leaf.append(i)
        minCost[i]=cost[i]
for i in range(0,len(leaf)):
    res=res+present[leaf[i]]*cost[leaf[i]]

    root=Tree[leaf[i]]
    while root!=-1:
        x=present[root]-present[leaf[i]]
        if x>0:
            present[root]=x
        else:
            present[root]=0
        minCost[root]=min(minCost[root],minCost[leaf[i]])
        root=Tree[root]
    present[leaf[i]]=0
for i in range(1,n+1):
    if present[i]!=0:
        res=res+minCost[i]*present[i]
        root=Tree[i]
        while root!=-1:
            z=present[root] - present[i]
            if z>0:
                present[root] =z
            else:
                present[root]=0
            root = Tree[root]
print(res)