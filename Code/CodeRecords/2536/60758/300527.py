travel=eval(input())
total=[]
fin=[1 for i in range(len(travel))]
for i in travel:
    for j in i:
        if j not in total:
            total.append(j)
out=[]
visited=[0 for i in range(len(travel))]
def deep(cp,temp,visited):
    if visited==fin:
        out.append(temp)
    for i in range(len(travel)):
        x=travel[i][0]
        y=travel[i][1]
        if x==cp and visited[i]==0:
            visited[i]=1
            temp.append(y)
            deep(y,temp.copy(),visited.copy())
            visited[i]=0
            temp=temp[0:len(temp)-1]
deep("JFK",["JFK"],visited)
out.sort()
print(out[0])