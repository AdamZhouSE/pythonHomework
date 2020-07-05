N = int(input())
values = [int(x) for x in input().split()]
values = [0]+values
graph = {}
ans = 0
def dfs(pre,cur):
    global ans
    for i in graph[cur]:
        if i==pre:
            continue
        else:
            dfs(cur,i)
            values[cur]+=max(0,values[i])
    ans = max(ans,values[cur])

for i in range(N-1):
    fr,to = [int(x) for x  in  input().split()]
    if fr in graph:
        graph[fr].append(to)
    else:
        graph[fr] = [to]
    if to in graph:
        graph[to].append(fr)
    else:
        graph[to] = [fr]
dfs(0,1)
print(ans,end="")