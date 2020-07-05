t=int(input())
for i in range(t):
    n_p=input().split()
    n=int(n_p[0])
    p=n_p[1]
    alls=input().split(" ")
    sources=[]
    for i in range(n):
        x=input().split(" ")
        sources.append(x[1:])
    res=[]
    res.append(p)
    ans=[]
    while(len(res)>0):
        a=[]
        for j in res:
            ans.append(j)
            for h in range(n):
                if sources[alls.index(j)][h]==1:
                    if not alls[h] in ans and not alls[h] in a:
                        a.append(alls[h])
    print(*ans)
        
                        
    