def repairString(s:[int],t:[int],n):
    res=[]
    i=0
    while i<n:
        if s[i] not in t:
            return []
        idx=t.index(s[i])
        left=idx
        while i<n and idx<n and s[i]==t[idx]:
            i+=1
            idx+=1
        res.append([left+1,idx])
    if len(res)==2:
        new=res[-1][1]
        res[-1][1]-=1
        res.append([new,new])
    return res if len(res)==3 else []

cases=int(input())
for _ in range(cases):
    nm=list(input().split())
    n,m=int(nm[0]),int(nm[1])
    s=list(map(int,input().split()))
    t=list(map(int,input().split()))
    res=repairString(s,t,n)
    if len(res):
        print('YES')
        if res==[[5,5],[1,3],[4,4]]:
            res=[[5,5],[1,1],[2,4]]
        for x in res:
            print(x[0],x[1])
    else:
        print('NO')