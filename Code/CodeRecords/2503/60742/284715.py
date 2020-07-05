def dfs(root,father):
    global f
    tmp = [0,0]
    for i in range(2*(n-1)):
        if e1[i]==root and e2[i]!=father:
            dfs(e2[i],root)
            tmp.append(f[e2[i]][0]+1)
    tmp.sort(reverse=True)
    f[root][0] = tmp[0]
    f[root][1] = tmp[1]
    return

n = int(input())
e1 = []
e2 = []
f = [[0,0] for i in range(n+1)]
for i in range(n-1):
    s = [int(i) for i in input().split()]
    e1.append(s[0])
    e2.append(s[1])
    e1.append(s[1])
    e2.append(s[0])
dfs(1,0)
res = 0
for i in range(1,n+1):
    res = max(res,f[i][0]+f[i][1])
print(res)