def findRDC(edges:[[int]]):
    n=len(edges)
    father=list(range(n+1))
    indeg=[0]*(n+1)
    def find(x):
        f=x
        while f!=father[f]:
            f=father[f]
        while f!=x:
            x,father[x]=father[x],f
        return f

    def union(x,y):
        father[find(y)]=find(x)

    lastA,lastB,dpA,dpB=-1,-1,-1,-1
    for a,b in edges:
        indeg[b]+=1
        if indeg[b]==2:
            dpA,dpB=a,b
        fa,fb=find(a),find(b)
        if fa!=fb:
            union(a,b)
        else:
            lastA,lastB=a,b

    if dpB==-1:
        return [lastA,lastB]
    father,firstA=list(range(n+1)),-1
    for a,b in edges:
        if b!=dpB:
            fa,fb=find(a),find(b)
            if fa!=fb:
                union(a,b)
            else:
                return [firstA,dpB]

    return [dpA,dpB]

edges=eval(input())
print(findRDC(edges))