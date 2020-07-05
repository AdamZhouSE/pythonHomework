def dfs(s):
    ans.append(s)
    while(s in graph):
        if(not graph[s]):
            return
        nxt=graph[s][0]
        del graph[s][0]
        dfs(nxt)
ticket=eval(input())
graph={}
for i in ticket:
    graph.setdefault(i[0],[]).append(i[1])
for i in graph.values():
    i.sort()
ans=[]
dfs('JFK')
print(ans)