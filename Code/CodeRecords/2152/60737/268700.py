n = int(input())
INF = 999
orz = [int(i) for i in input().split( )]
d = [0]*INF
f = [int(i) for i in input().split( )]
for i in f:
    d[i] += 1
ans = [0]*INF
vis = [0]*INF
que, stk = [], []


def top_sort():
    for i in range(1, n+1):
        if d[i]:
            que.append(i)
        while que:
            t = que.pop(0)
            stk.append(t)
            d[f[t]] -= 1
            if d[f[t]]:
                que.append(f[t])

                
def dfs(u, root):
    if vis[u]:
        return
    vis[u] = 1
    ans[root] += orz[u]
    q.append(u)
    dfs(f[u], root)
    
    
def circle():
    for i in range(1, n+1):
        if d[i] and not vis[i]:
            dfs(i, i)
            while que:
                t = que.pop(0)
                ans[t] = ans[i]

                
top_sort()
circle()
while stk:
    t = stk.pop()
    ans[t] = orz[t] + ans[f[t]]
for i in range(1, n+1):
    print(ans[i])
    