from itertools import combinations
t=int(input())
for j in range(t):
    n=int(input())
    source=input().split(" ")
    sources=[]
    for a in source:
        sources.append(int(a))
    g_sum=int(input())
    targets=[]
    for i in range(n):
        target=list(combinations(sources,i))
        for a in target:
            x=[]
            for b in a:
                x.append(b)
            targets.append(x)
    sums=[]
    for i in targets:
        sum=0
        for a in i:
            sum=sum+a
        if(sum==g_sum):
            sums.append(sum)
    print(len(sums))