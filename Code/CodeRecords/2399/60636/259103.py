from itertools import permutations,product
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
        sources.append(int(i))
    targets=[]
    for i in range(m-len(lists),m+1):
        target=product(lists,i)
        print(target)
