n,r,avg=map(int,input().split(' '))
a=[[0 for i in range(2)] for i in range(n)]
avg*=n
for i in range(n):
    a[i][1],a[i][0]=map(int,input().split(' '))
    avg-=a[i][1]
    a[i][1]=r-a[i][1]
a.sort()
ans=0
for i in range(n):
    if avg<=0:
        break
    if a[i][1]>=avg:
        ans+=avg*a[i][0]
        break
    else:
        ans+=a[i][1]*a[i][0]
        avg-=a[i][1]
print(ans)
