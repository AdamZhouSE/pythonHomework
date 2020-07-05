def union(a,b):
    global f
    f[a]=b

def getf(x):
    while x!=-1:
        x=f[x]
    return x

stones=eval(input())
n=len(stones)
f=[-1 for i in range(0,n)]
for i in range(0,n):
    for j in range(i+1,n):
        if(stones[i][0]==stones[j][0])or(stones[i][1]==stones[j][1]):
            union(i,j)
ans=n
for i in range(0,n):
    if f[i]==-1:
        ans-=1
print(ans)