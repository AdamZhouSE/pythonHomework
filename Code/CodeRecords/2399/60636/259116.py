from itertools import permutations,combinations_with_replacement
t=int(input())
for j in range(t):
    n_m_l_r=input().split(" ")
    n=int(n_m_l_r[0])
    m=int(n_m_l_r[1])
    l=int(n_m_l_r[2])
    r=int(n_m_l_r[3])
    lists=[]
    for i in range(l,m+1):
        lists.append(i)
    source=input().split(" ")
    sources=[]
    for i in source:
        if i!="":
            sources.append(int(i))
    targets=[]
    target=list(combinations_with_replacement(lists,m))
    print(target)
