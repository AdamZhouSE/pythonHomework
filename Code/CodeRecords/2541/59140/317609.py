def dfs(i, adj, flag, res):
    if flag[i] == 1:
        return True
    elif flag[i] == -1:
        return False
    flag[i] = -1
    for j in adj[i]:
        if not dfs(j, adj, flag, res): return False
    flag[i] = 1
    res.append(i)
    return True

n=int(input())
temp=input()[2:-2].split("],[")
ans=[]
for i in temp:
    ans.append([int(x) for x in i.split(",")])
adj = [[] for _ in range(n)]
flag = [0] * n
for p in ans:
    adj[p[0]].append(p[1])  # 构造的图是p[0]->p[1]
res = []
for i in range(n - 1, -1, -1):  # 最后遍历的时候要从numcourse-1开始
    if not dfs(i, adj, flag, res):
        res=[]
        break
print(res)
