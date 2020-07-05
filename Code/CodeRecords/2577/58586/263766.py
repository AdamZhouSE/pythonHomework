start=list(map(int,input().split(",")))
end=list(map(int,input().split(",")))
profit=list(map(int,input().split(",")))
point=[]
graph=[[0]*len(start) for c in range(len(start))]
for i in range(len(start)):
    point.append((start[i],end[i],profit[i]))
point.sort(key=lambda x:x[0])
# print(point)
for i in range(len(point)):
    graph[i][i]=1
    for j in range(i+1,len(point)):
        if point[j][0]>=point[i][1]:
            graph[i][j]=1
def dfs(graph,sum,pre,start,ans):
    if sum>ans[0]:
        ans[0]=sum
    for i in range(start,len(graph)):
        if graph[pre][i]:
            dfs(graph,sum+point[i][2],i,i+1,ans)
ans=[0]
dfs(graph,0,0,0,ans)
print(ans[0])



