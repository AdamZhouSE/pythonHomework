t=int(input())
for i in range(0,t):
    n,m=map(int,input().split())
    a=[int(n) for n in input().split()]
    b=[int(m) for m in input().split()]
    re=[]
    for j in a:
        if j not in re:
            re.append(j)
    for c in b:
        if c not in re:
            re.append(c)
    print(len(re))
