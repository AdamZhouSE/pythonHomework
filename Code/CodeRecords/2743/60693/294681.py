from collections import defaultdict

def findPath(graph:{},start,end,path=[]):
    path=path+[start]
    if start==end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath=findPath(graph,node,end,path)
            if newpath:
                return newpath
    return None


n=int(input())
show_order=list(map(int,input().split()))
graph=defaultdict(list)
for _ in range(n-1):
    connec=list(map(int,input().split()))
    graph[connec[0]].append(connec[1])
    graph[connec[1]].append(connec[0])

candy=[0 for i in range(n)]
# candy[show_order[0]-1]+=1
for i in range(n-1):
    path=findPath(graph,show_order[i],show_order[i+1])
    path.pop(-1)
    for j in path:
        candy[j-1]+=1
# candy[show_order[-1]-1]-=1
for x in candy:
    print(x)