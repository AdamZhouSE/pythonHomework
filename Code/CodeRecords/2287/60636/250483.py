t=int(input())
for j in range(t):
    n=int(input())
    source=input().split(" ")
    sources=[]
    for i in source:
        sources.append(int(i))
    res=[]
    for i in range(len(sources)):
        k=len(res)
        for a in range(i+1,len(sources)):
            if(sources[a]>sources[i]):
                res.append(sources[a])
                break
        if(k==len(res)):
            res.append(-1)
    print(*res)