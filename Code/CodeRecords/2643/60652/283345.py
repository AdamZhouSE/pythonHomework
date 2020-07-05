def angry_boss():
    c=list(map(int,input().split(',')))
    g=list(map(int,input().split(',')))
    X=int(input())
    satis=0
    for i in range(len(c)):
        if g[i]==0:
            satis+=c[i]
    l,r=0,X
    res=0
    while r<=len(c):
        add=0
        for j in range(l,r):
            if g[j]==1:
                add+=c[j]
        res=max(satis+add,res)
        l+=1
        r+=1
    return res


print(angry_boss())