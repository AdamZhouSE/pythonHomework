n=int(input())
x=[0 for i in range(n+1)]
h=[0 for i in range(n+1)]
dpx=[0 for i in range(n+1)]
for i in range(n):
    x[i],h[i]=map(int,input().split())
ans=1
dpx[0]=x[0]
for i in range(1,n):
    if(x[i]-h[i]>dpx[i-1]):
        dpx[i]=x[i]
        ans+=1
    elif(x[i]+h[i]<x[i+1]):
        dpx[i]=x[i]+h[i]
        ans+=1
    elif(i==n-1):
        ans+=1
    else:
        dpx[i]=x[i]
print(ans)