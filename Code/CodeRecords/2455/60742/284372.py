def dfs(root,father):
    global f
    tmp = []
    for i in range(2*(n-1)):
        if e1[i]==root and e2[i]!=father:
            dfs(e2[i],root)
            f[root] += max(0,f[e2[i]])
    return

n = int(input())
f = [int(i) for i in input().split()]
f.insert(0,0)
e1 = []
e2 = []
for t in range(n-1):
    s = [int(i) for i in input().split()]
    e1.append(s[0])
    e2.append(s[1])
    e1.append(s[1])
    e2.append(s[0])
dfs(1,0)
res = max(f)
print(res,end='')