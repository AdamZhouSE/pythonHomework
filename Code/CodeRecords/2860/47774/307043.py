def dfs(i):
    v[i]=1
    for j in range(n):
        if v[j]==0 and (x[i]==x[j] or y[i]==y[j]):
            dfs(j)

n=int(input())
x=[0 for i in range(1000)]
y=[0 for i in range(1000)]
v=[0 for i in range(1000)]
for i in range(n):
    x[i],y[i]=map(int,input().split(' '))
ans=0
for i in range(n):
    if v[i]==0:
        dfs(i)
        ans+=1
print(ans-1)