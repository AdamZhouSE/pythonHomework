def minheight(i,edges):
    ans=10000
    temp=[]
    if(not edges):
        return 0
    j=0
    while(j<len(edges)):
        if(edges[j][0]==i or edges[j][1]==i):
            temp.append(edges.pop(j))
        else:
            j+=1
    for edge in temp:
        if(edge[0]==i):
            ans=min(ans,1+minheight(edge[1],edges[:]))
        else:
            ans=min(ans,1+minheight(edge[0],edges[:]))
    return ans
            

n=int(input())
edges=eval(input())
node=[i for i in range(n)]
minh=[n for i in range(n)]
for i in range(n):
    minh[i]=minheight(i,edges[:])
j=min(minh)
ans=[]
for i in range(len(minh)):
    if minh[i]==j:
        ans.append(i)
print(ans)
