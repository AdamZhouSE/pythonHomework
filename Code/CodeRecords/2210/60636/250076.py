t=int(input())
for a in range(t):
    sources=list(input())
    targets=list(input())
    print(targets)
    res=[]
    start=0
    x=0
    for i in targets:
        print(i)
        while(sources[x]!=i):
            print(x)
            x=x+1
            if(x==len(sources)-1):
                break
        if(x==len(sources)-1):
            break
        else:
            res.append(sources[start:x+1])
        x=x+1
        start=x
    print(res)