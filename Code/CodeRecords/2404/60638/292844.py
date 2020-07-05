inpu=list(map(int,input().split(" ")))
n=inpu[0]
s=inpu[1]
leaf=[1]*n
values=list(map(int,input().split(" ")))
nodes=[-1]*n
for i in range(0,n-1):
    x=input().split(" ")
    y=[]
    for j in range(0,len(x)):
        if x[j]!="":
            y.append(int(x[j]))
    nodes[y[1]-1]=y[0]-1
count=0
for i in range(0,n):
    root=nodes[i]
    sum=values[i]
    if sum==s:
        count=count+1
    while root!=-1:
        sum=sum+values[root]
        if sum==s:
            count=count+1
            break
        if sum>s:
            break
        root=nodes[root]
print(count)