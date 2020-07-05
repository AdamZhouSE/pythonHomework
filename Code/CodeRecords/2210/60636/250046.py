t=int(input())
for a in range(t):
    sources=list(input())
    targets=list(input())
    res=[]
    start=0
    x=0
    for i in targets:
        while(sources[x]!=i):
            x=x+1
            if(x==len(sources)):
                break
        if(x==len(sources)):
            break
        else:
            res.append(sources[start:x+1])
        x=x+1
        start=x
    print(res)