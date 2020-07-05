n=int(input())
x=[0 for i in range(1001)]
y=[0 for i in range(1001)]
E=[]
for i in range(n):
    xx,yy=map(int,input().split())
    E.append((xx,yy))
    x[xx]+=1
    y[yy]+=1
ans=0
for i in E:
    if(x[i[0]]==1 and y[i[1]]==1):
        ans+=1
print(ans-1)