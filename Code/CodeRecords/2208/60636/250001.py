t=int(input())
for j in range(t):
    n=int(input())
    source=input().split(" ")
    sources=[]
    for i in source:
        sources.append(int(i))
    res=[]
    for i in range(len(sources)):
        if(i==0):
            res.append(-1)
        else:
            k=len(res)
            for a in range(i-1,-1,-1):
                if(sources[a]<sources[i]):
                    res.append(sources[a])
                    break
            if(len(res)==k):
                res.append(-1)
    print(*res)