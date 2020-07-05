n=int(input())
x=[0 for i in range(1001)]
y=[0 for i in range(1001)]
ans=0
for i in range(n):
    xx,yy=map(int,input().split())
    if(x[xx]==0 and y[yy]==0):
        x[xx]=1
        y[yy]=1
        ans+=1
print(ans-1)