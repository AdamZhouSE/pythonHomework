n=int(input())
x=[0 for i in range(n)]
h=[0 for i in range(n)]
dpx=[0 for i in range(n)]
for i in range(n):
    x[i],h[i]=map(int,input().split())
ans=1
for i in range(1,n-1):
    if(x[i]-h[i]>dpx[i-1]):
        dpx[i]=x[i]
        ans+=1
    elif(x[i]+h[i]<x[i+1]):
        dpx[i]=x[i]+h[i]
        ans+=1
    else:
        dpx[i]=x[i]
ans+=1
print(ans)