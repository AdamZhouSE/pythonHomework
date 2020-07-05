
import sys
import re
import math
n = 0
f = [0] * 1000
visit = [0] * 1000
graph = [[0]] * 1000
for i in range(1000):
    lists=[]
    graph[i]=lists
val = [0] * 1000
def dfs(x):
    if f[x] > 0:
        return
    f[x] = val[x]
    for i in range(len(graph[x])):
        y = graph[x][i]
        if visit[y] == 0:
            visit[y] = 1
            dfs(y)
            f[x] += max(0, f[y])                                    
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
slists=s.split("\n")
nums= [int(e) for e in digits ]
n = nums[0]
del (nums[0])
for i in range(1, n + 1):
    val[i] = nums[0]
    del (nums[0])
for j in range(n-1):
    x = nums[2*j]
    y = nums[2*j+1]
    graph[x].append(y)
    graph[y].append(x)
visit[1] = 1
dfs(1)
ans = 0
for i in range(n + 1):
    ans = max(ans, f[i])
sys.stdout.write(str(ans))
