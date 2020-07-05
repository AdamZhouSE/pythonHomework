from itertools import combinations
t=int(input())
for j in range(t):
    k=int(input())
    n=int(input())
    source=input().split(" ")
    sources=[]
    for i in source:
        sources.append(int(i))
    lists=[]
    for i in range(n):
        lists.append(i)
    target=list(combinations(lists,2))
    target_0=[]
    for z in target:
        x=[]
        for a in z:
            x.append(a)
        target_0.append(x)
    target_1=[]
    for i in range(0,k+1):
        target_x=list(combinations(target_0,k))
        for a in target_x:
            target_1.append(a)
    targets=[]
    for z in target_1:
        pos=True
        for a in range(len(z)-1):
            if(z[a][1]>z[a+1][0]):
                pos=False
        if(pos):
            x=[]
            for a in z:
                x.append(a)
            targets.append(x)
    res=[]
    for i in targets:
        re=[]
        for a in i:
            re.append(sources[a[1]]-sources[a[0]])
        res.append(re)
    sums=[]
    for i in res:
        sum=0
        for a in i:
            sum=sum+a
        sums.append(sum)
    if(max(sums)==70):
        print(sources)
        print(k)
        print(targets)
        print(res)
        print(sums)
    print(max(sums))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            