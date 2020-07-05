def dfs(x):
    if p[x]!=0:
        return p[x]
    p[x]=dfs(x-2)+dfs(x-3)
    return p[x]


p = [0 for x in range(100)]
p[0]=p[1]=p[2]=1
t = int(input())
for i in range(t):
    print(dfs(int(input())))