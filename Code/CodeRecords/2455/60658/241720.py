def dfs(pre,cur):
    global ans
    for i in graph[cur]:
        if i==pre:
            continue
        # print("start dfs from %d to %d"%(cur,i))
        dfs(cur,i)
        # print("end dfs from %d to %d"%(cur,i))
        values[cur]+=max(values[i],0)
        # print(values)
    ans = max(ans,values[cur])

ans = 0
n = int(input())
values = [int(x) for x in input().split()]
values = [0]+values
graph = {}
for i in range(n-1):
    fr,to = [int(x) for x in input().split()]
    if fr in graph:
        graph[fr].append(to)
    else:
        graph[fr]=[to]
    if to in graph:
        graph[to].append(fr)
    else:
        graph[to]=[fr]
# print(graph)
dfs(0,1)
print(ans,end="")