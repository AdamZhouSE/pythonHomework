n=int(input())
u,v,w=[],[],[]
for i in range(n):
    uvw=input().split(' ')
    u.append(int(uvw[0]))
    v.append(int(uvw[1]))
    w.append(int(uvw[2]))
m=int(input())
for i in range(m):
    se=input().split(' ')
    s=int(se[0])
    e=int(se[1])
    