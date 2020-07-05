n,m=map(int,input().split(' '))
x=[0 for i in range(n)]
y=[0 for i in range(n)]
z=[0 for i in range(n)]
sum=0
flag=1
for i in range(n):
    x[i],y[i]=map(int,input().split(' '))
    z[i]=x[i]-y[i]
    sum+=y[i]
if sum>m:
    print(-1)
else:
    z.sort()
    ans=0
    for i in range(n):
        if sum+z[i]<=m:
            sum+=z[i]
            ans+=1
        else:
            break
    print(n-ans)
        