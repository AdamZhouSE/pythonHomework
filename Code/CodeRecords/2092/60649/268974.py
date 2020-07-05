def dfs(x,z):
    global max1
    while u[x]!=now:
        v[x]=z
        u[x]=now
        x=a[x]
        z+=1
    max1=min(max1,z-v[x])
def dell(x):
    k=a[x]
    a[x]=0
    v[k]-=1
    if v[k]==0:
        dell(k)
n=int(input())
a=list(map(int,input().split()))
a=[0]+a
max1,now=9999999999,0
v=[0 for i in range(200001)]
u=[i for i in range(200001)]
for i in range(1,n+1):
    v[a[i]]+=1
for i in range(1,n+1):
    if v[i]==0:
        dell(i)
v=[0 for i in range(200001)]
for i in range(1,n+1):
    now=i
    if v[i]==0 and a[i]!=0:
        v[i]=1
        dfs(a[i],2)
print(max1)
