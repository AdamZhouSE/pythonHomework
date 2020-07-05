t=int(input())
for a in range(t):
    sources=list(input())
    targets=list(input())
    res=[]
    start=0
    a=0
    for i in targets:
        while(targets[a]!=i):
            a=a+1
            if(a==len(targets)):
                break
        if(a==targets):
            break
        else:
            res.append(sources[start:a+1])
        a=a+1
        start=a
    print(res)