def dfs(pre,cur,dep):
    ans=0
    ma1,ma2=0,0
    for child in edges[cur]:
        if child==pre: continue
        # print("  "*dep+"start dfs %d %d"%(cur,i))
        dfs(cur,child,dep+1)
        # print("  "*dep+"end dfs %d %d"%(cur,i))
        if first[child]+1>first[cur]:
            second[cur]=first[cur]
            first[cur]=first[child]+1
        elif first[child]+1>second[cur]:
            second[cur]=first[child]+1
        # print("  "*dep+"first update"+str(first))
        # print("  "*dep+"second update"+str(second))
    
    return 

n = int(input())
edges = {}
first = [0]*(n+1)
second = [0]*(n+1)
for i in range(n-1):
    fro,to = [int(x) for x in input().split()]
    if fro in edges:
        edges[fro].append(to)
    else:
        edges[fro]=[to]
    if to in edges:
        edges[to].append(fro)
    else:
        edges[to]=[fro]
dfs(0,1,0)
print(first[1]+second[1])