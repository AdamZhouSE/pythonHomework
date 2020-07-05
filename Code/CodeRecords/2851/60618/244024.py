n=int(input())
x=['']*n
y=['']*n
for i in range(0,n):
    x[i],y[i]=map(int,input().split())
side=0
for i in range(0,n):
    if x[i]+y[i]>side:
        side=x[i]+y[i]
print(side)