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
    target_1=list(combinations(target_0,k))
    targets=[]
    for z in target_1:
        pos=True
        for a in range(len(z)-1):
            if(z[a][1]>z[a+1][0]):
                pos=False
        if(pos):
            x=[]
            for a in z:
                x.append(sources[a])
            targets.append(x)
    print(targets)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            