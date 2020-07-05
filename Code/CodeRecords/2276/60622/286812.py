R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
ans=[[r0,c0]]
r=0
c=1
n=0
step=1
while len(ans)<R*C:
    for i in range(step):
        r0+=r
        c0+=c
        if 0<=r0<R  and 0<=c0<C:
            ans.append([r0,c0])
    n+=1
    if n%2==0:
        step+=1
    r,c=c,r
    c=-c
print(ans)