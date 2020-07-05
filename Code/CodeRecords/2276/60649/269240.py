R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
res=[[r0,c0]]
r,c,n,step=0,1,0,1
while len(res)<R*C:
    for i in range(step):
        r0+=r
        c0+=c
        if 0<=r0<R and 0<=c0<C:
            res.append([r0,c0])
    n += 1
    if n % 2 == 0:
        step += 1
    r, c = c, r
    c=-c
print(res)