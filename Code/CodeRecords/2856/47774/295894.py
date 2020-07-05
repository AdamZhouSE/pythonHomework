n=int(input())
x=[0 for i in range(n)]
h=[0 for i in range(n)]
d=[0 for i in range(n)]
for i in range(n):
    x[i],h[i]=map(int,input().split(' '))
for i in range(1,n):
    d[i]=x[i]-x[i-1]
d[0]=0
sum=2
for i in range(1,n-1):
    if h[i]<d[i]:
        sum+=1
    elif h[i]>=d[i] and h[i]<d[i+1]:
        sum+=1
        d[i+1]-=h[i]
print(sum)
        