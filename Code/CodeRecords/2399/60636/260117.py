from itertools import permutations,combinations_with_replacement
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
    print(sources)
