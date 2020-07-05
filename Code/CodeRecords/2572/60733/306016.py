k, y,t =map(int, input(). split())
l=[1 for i in range(k)]
for i in range(t):
    tmp=input(). split()
    tmp[1: ]=map(int, tmp[1: ])
    le=min(tmp[1], tmp[2])
    ri=max(tmp[1], tmp[2])
    if tmp[0]=='C':
        l[le-1: ri]=[tmp[3] for i in range(ri-le+1)]
    else:
        print(len(set(l[le-1: ri])))
