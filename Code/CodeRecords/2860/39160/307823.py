n = int(input())
p = []
 
def dfs(i):
    p[i][-1] = res
    for j in range(n):
        if p[j][-1] == -1 and (p[i][0] == p[j][0] or p[i][1] == p[j][1]):
            dfs(j)

res = -1
for i in range(n):
    x, y = map(int, input().split())
    p.append([x, y, -1])
for i in range(n):
    if p[i][-1] == -1:
        res += 1
        dfs(i)
print(res)