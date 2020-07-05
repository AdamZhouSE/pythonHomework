t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    a=input().split(' ')
    a=list(map(int,a))
    l=[]
    while len(a)>0:
        rising=set()
        head=a.pop(0)
        rising.add(head)
        tail=head
        while len(a)>0 and a[0]>=head:
            tail=a.pop(0)
            head=tail
        rising.add(tail)
        rising=list(rising)
        rising.sort()
        if len(rising)>=2:
            l.append(rising)
    while len(l)>k:
        merged=[]
        len_l=len(l)
        for j in range(len_l-1):
            x=l[j]
            y=l[j+1]
            merged.append(y[1]-x[0])
        toMerge=max(merged)
        toMerge=merged.index(toMerge)
        x=l[toMerge]
        y=l[toMerge+1]
        l[toMerge]=[x[0],y[1]]
        l.pop(toMerge+1)
    money=0
    for e in l:
        money+=e[1]-e[0]
    print(money)