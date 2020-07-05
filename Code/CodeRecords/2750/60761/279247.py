def minheight(i,edges):
    ans=10000
    temp=[]
    if(not edges):
        return 0
    for edge in edges:
        if(edge[0]==i or edge[1]==i):
            temp.append(edge)
    edges=list(set(edges)-set(temp))
    for edge in temp:
        if(edge[0]==i):
            ans=min(ans,1+minheight(edge[1],edges))
        else:
            ans=min(ans,1+minheight(edge[0],edges))
            

n=int(input())
edges=eval(input())
node=[i for i in range(n)]
minh=[n for i in range(n)]
for i in range(n):
    minh[i]=minheight(i,edges)
j=min(minh)
ans=[]
for i in range(len(minh)):
    if minh[i]==j:
        ans.append(i+1)
print(ans)
