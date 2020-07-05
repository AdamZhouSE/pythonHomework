vertex=int(input())
degree={}
edges=[]
for i in range(vertex-1):
    edge=list(map(int,input().strip().split(" ")))
    edges.append(edge)
    degree[edge[0]]=degree[edge[0]]+1 if edge[0] in degree.keys() else 1
    degree[edge[1]] = degree[edge[1]] + 1 if edge[1] in degree.keys() else 1
pre=edges.copy()
while True:
    delete=[]
    for e in edges:
        if degree[e[0]]>1 and degree[e[1]]>1:
            delete=e.copy()
            edges.remove(e)
            break
    for e in edges:
        if e[0] in delete:
            degree[e[0]]-=1
        if e[1] in delete:
            degree[e[1]]-=1
    if len(delete)==0:
        break
mul=1
used=[]
while len(used)<len(edges):
    temp=[]
    for i in range(len(edges)):
        if i in used:
            continue
        else:
            temp.append(edges[i][0])
            temp.append(edges[i][1])
            used.append(i)
            for j in range(len(edges)):
                if j not in used:
                    if edges[j][0] in temp and edges[j][1] not in temp:
                        temp.append(edges[j][1])
                        used.append(j)
                    elif edges[j][1] in temp and edges[j][0] not in temp:
                        temp.append(edges[j][0])
                        used.append(j)
            mul *= len(temp)
            temp.clear()
print(mul)