edges:list=eval("["+input()+"]");
edges.sort(reverse=False);
# print(edges)
result=0;
for i in range(len(edges)-3,-1,-1):
    if(edges[i]+edges[i+1]>edges[i+2]):
        result=max(result,edges[i]+edges[i+1]+edges[i+2])
print(result)