n=int(input())
li=eval(input())

#深度优先，1 访问过
def dfs(i, adh, flag, res):
    if flag[i]==1:
        return True
    elif flag[i]==-1:
        return False
    flag[i] = -1
    for j in adh[i]:
        if not dfs(j, adh, flag, res):
            return False
    flag[i] = 1
    res.append(i)
    return True
        
adj = [[] for i in range(n)]#一对多
flag = [0]*n
for p in li:
    adj[p[0]].append(p[1])
res=[]
for i in range(n):
    if not dfs(i, adj, flag, res):
        break
print(res)