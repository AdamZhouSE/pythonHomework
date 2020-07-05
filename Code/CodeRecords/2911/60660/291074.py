def find(x):
    while f[x]!=-1:
        x=f[x]
    return x
def union(x,y):
    f[find(x)]=y
l=eval('['+input().replace(' ',',')+']')
n=l[0]
m=l[1]
l=eval('['+input().replace(' ',',')+']')
f=[-1 for i in range(n)]
for i in range(m):
    r=eval('['+input().replace(' ',',')+']')
    if l[find(r[0]-1)]<l[find(r[1]-1)]:
        union(r[1]-1,r[0]-1)
    else:
        union(r[0]-1,r[1]-1)
result=0
for i in range(n):
    if f[i]==-1:
        result+=l[i]
print(result)