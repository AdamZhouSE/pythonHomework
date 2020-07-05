t=int(input())
for j in range(t):
    n_m=input().split(" ")
    n=int(n_m[0])
    m=int(n_m[1])
    n_source=[]
    x=input().split(" ")
    for i in x:
        n_source.append(int(i))
    m_source=[]
    y=input().split(" ")
    for i in y:
        m_source.append(int(i))
    all_n=[]
    for i in n_source:
        if(not i in all_n):
            all_n.append(i)
    all_m=[]
    for i in m_source:
        if(not i in all_m):
            all_m.append(i)
    all=[]
    for i in all_n:
        if(i in all_m):
            all.append(i)
    print(len(all))