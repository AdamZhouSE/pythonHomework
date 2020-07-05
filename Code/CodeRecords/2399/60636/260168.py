def jiecheng(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res
t=int(input())
for j in range(t):
    n_m_l_r=input().split(" ")
    n=int(n_m_l_r[0])
    m=int(n_m_l_r[1])
    l=int(n_m_l_r[2])
    r=int(n_m_l_r[3])
    source=input().split(" ")
    sources=[]
    for i in source:
        if i!="":
            sources.append(int(i))
    while(m>0):
        counts=[]
        for i in range(l,r+1):
            count=0
            for x in sources:
                conunt=count+1
            counts.append(count)
        sources.append(counts.index(min(counts))+l)
        m=m-1
    alls=[]
    for i in sources:
        if not i in alls:
            alls.append(i)
    counts_0=[]
    for i in alls:
        count_0=0
        for x in sources:
            if x==i:
                count_0+=1
        counts_0.append(count_0)
    print(counts_0)
    res=jiecheng(len(sources))
    for i in counts_0:
        res=res/(jiecheng(i))
    print(res)
    print(sources)
