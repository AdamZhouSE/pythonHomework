n=int(input())
a=[0]*(n+1)
b=[0]*(n+1)
ans=[]
for i in range(1,n*n+1):
    x,y=map(int,input().split())
    if a[x]+b[y]==0: ans+=[str(i)]; a[x]=1; b[y]=1
print(' '.join(ans))