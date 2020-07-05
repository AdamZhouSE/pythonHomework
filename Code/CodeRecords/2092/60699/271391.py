
n=int(input())
list1=list(map(int,input().split(' ')))
N=200005
a=[0]
for i in list1:
    a.append(i)
vis=[]
t=0
for i in range(N):
    vis.append(0)
ans=N+1
def dfs(x):
    global t
    start= t+1
    while vis[x]==0:
        t+=1
        vis[x]=t
        x=a[x]
    if start>vis[x]:
        return N+1
    else:
        return t-vis[x]+1
for i in range(1,n+1):
    if vis[i]==0:
        ans=min(ans,dfs(i))
print(ans,end="")