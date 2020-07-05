from functools import cmp_to_key
def cmp(x,y):
    if x[0]==y[0]:
        return -1 if x[2]>y[2] else 1
    else:
        return -1 if x[0]<y[0] else 11
k,n,c=map(int,input().split())
myd=[0 for i in range(c+1)]
myd[0]=10000000000
s=[100000000 for i in range(50001)]
s[0]=0
e=s.copy()
m=[0 for i in range(50001)]
for i in range(1,k+1):
    s[i],e[i],m[i]=map(int,input().split())
z=zip(e,m,s)
z=sorted(z,key=cmp_to_key(cmp))
res=0
for i in range(1,k+1):
    myd.sort(reverse=True)
    j,tmp=1,z[i][1]
    while j<=c and tmp>0:
        if myd[j]<=z[i][2]:
            res+=1
            myd[j]=z[i][0]
            tmp-=1
        j+=1
print(res)
